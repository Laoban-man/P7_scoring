import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import lime
from lime import lime_tabular
import matplotlib.pyplot as plt
import shap
import lightgbm as lgb


class Model:
    def __init__(self, X=[], y=[], params=[]):
        self.X = X
        self.y = y
        self.imputer = []
        self.scaler = []
        self.model = []

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
        self.X_sample = self.X.sample(frac=0.1)
        self.fitted_neighbours = self.neighbours.fit(self.X_sample)
        pickle.dump(self.neighbours, open("saved_neigbours.pkl", "wb"))

    def predict_cluster(self, candidate):
        cluster = self.neighbours.predict(candidate)
        return cluster

    def predict(self, new_data=[], import_mod=True):
        if import_mod == True:
            self.import_model(model_file="model.pkl")
        if type(new_data) != type(None):
            try:
                new_data = self.imputer.transform(new_data)
                new_data = self.scaler.transform(new_data)
                self.new_data = new_data
                new_data = np.array(new_data).reshape(1, 44)
                y_pred = self.model.predict_proba(new_data)
                y_pred = (y_pred[:, 1] > 0.5) + 0
                print(y_pred)
                self.result = y_pred
            except:
                print("The input is a nd array 1xn")
        else:
            try:
                y_pred = self.model.predict_proba(self.X_test)
                y_pred = (y_pred[:, 1] > 0.5) + 0
                self.result = y_pred
            except:
                print("No data was likely in the defined instance")
        try:
            self.interpretability()
        except:
            print("Error with interpretability")

        return self.result

    def interpretability(self):
        """Interpretability"""
        # Local interpretability
        explainer = lime_tabular.LimeTabularExplainer(
            training_data=np.array(self.X_sample),
            feature_names=self.X.columns,
            class_names=["0", "1"],
            mode="classification",
        )
        new_data = pd.DataFrame(self.new_data, columns=self.X.columns)
        try:
            exp = explainer.explain_instance(
                data_row=new_data.iloc[0],
                predict_fn=self.model.predict_proba,
            )
        except Exception as e:
            print(e)
        exp.as_pyplot_figure()
        plt.savefig("./images/local.png")
        plt.clf()
        # Global interpretability
        shap_values = shap.TreeExplainer(self.model).shap_values(self.X_sample)
        shap.summary_plot(shap_values, self.X_sample, show=False)
        plt.savefig("./images/global.png")
        plt.clf()

    def import_model(self, model_file="model.pkl"):
        """Import pre-defined model"""
        model, imp, ss = pickle.load(open(model_file, "rb"))
        self.model = model
        self.imputer = imp
        self.scaler = ss
