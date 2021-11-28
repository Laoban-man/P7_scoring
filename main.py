import hug
import pandas as pd
import numpy as np
import model
from model import Model
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pickle

X, y = load_iris(return_X_y=True, as_frame=True)


@hug.get()
@hug.local()
def default_endpoint():
    """Default endpoint"""
    return {"message": "You've achieved the default endpoint"}


@hug.get("/prediction")
@hug.local()
def candidate(data: hug.types.delimited_list(","), hug_timer=3):
    """Export candidate application data and return scoring"""
    global model
    model = Model(X, y, "linear", [])
    model.split(0.5)
    model.fit()
    model.predict()
    return {"data": model.result[0]}


@hug.get("/get_data", output=hug.output_format.image("png"))
@hug.local()
def graph_data(variable: hug.types.text, hug_timer=3):
    """Export graph candidate application data"""
    n, bins, patches = plt.hist(
        X[variable], 50, density=True, facecolor="g", alpha=0.75
    )
    plt.axvline(X[variable].mean(), color="k", linestyle="dashed", linewidth=1)
    plt.xlabel(variable)
    plt.ylabel("Value")
    plt.title("Histogram of " + variable)
    plt.grid(True)
    plt.savefig("./images/" + variable + ".png")
    return "./images/" + variable + ".png"
