import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class Model:
    def __init__(self, X=[], y=[], model_type="linear", params=[]):
        self.X = X
        self.y = y
        if model_type == "linear":
            self.model = LinearRegression()
        elif model_type == "test1":
            self.model = model_type(params[0], params[1], params[2])
        elif model_type == "test2":
            self.model = model_type(params[0], params[1], params[2])

    def split(self, test_size):
        X = np.array(self.X)
        y = np.array(self.y)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

    def fit(self):
        self.fitted_model = self.model.fit(self.X_train, self.y_train)
        pickle.dump(self.model, open("saved_model.pkl", "wb"))

    def predict(self, new_data=None):
        if type(new_data) != np.array:
            try:
                self.result = self.model.predict(self.X_test)
            except:
                print("No data was likely in the defined instance")
            return
        else:
            self.result = self.model.predict(new_data)
        return self.result

    def save_model(self, model_file="saved_model.pkl"):
        pickle.dump(self.model, open(model_file, "wb"))

    def import_model(self, model_file="saved_model.pkl"):
        self.model = pickle.load(open(model_file, "rb"))
