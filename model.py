import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans


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

    def fit_neighbours(self):
        self.neighbours = KMeans()
        self.fitted_neighbours = self.neighbours.fit(self.X_train)
        pickle.dump(self.neighbours, open("saved_neigbours.pkl", "wb"))

    def predict_cluster(self, candidate):
        cluster = self.neighbours.predict(candidate)
        return cluster

    def predict(self, new_data=None):
        if type(new_data) != type(None):
            try:
                self.result = self.model.predict(new_data)
            except:
                print("The input is a nd array 1xn")
        else:
            try:
                self.result = self.model.predict(self.X_test)
            except:
                print("No data was likely in the defined instance")
        return self.result

    def save_model(self, model_file="saved_model.pkl"):
        pickle.dump(self.model, open(model_file, "wb"))

    def import_model(self, model_file="saved_model.pkl"):
        self.model = pickle.load(open(model_file, "rb"))
