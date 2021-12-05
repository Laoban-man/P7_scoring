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
def predict_candidate(hug_timer=3):
    """Export candidate application data and return scoring"""
    prediction = model.predict(np.array(candidate).reshape(1, 4))
    return {"prediction": prediction}


@hug.get("/post_data")
@hug.local()
def candidate(columns: hug.types.text, values: hug.types.text, hug_timer=3):
    global model
    global candidate
    model = Model(X, y, "linear", [])
    model.split(0.5)
    model.fit()
    model.fit_neighbours()
    values = np.array([float(a) for a in values.split(",")])
    values = values.reshape(1, values.shape[0])
    candidate = pd.DataFrame(values, columns=columns.split(","))
    return {"hello": "world"}


@hug.get("/get_data", output=hug.output_format.image("png"))
@hug.local()
def graph_data(variable: hug.types.text, mode: hug.types.number, hug_timer=3):
    """Export graph candidate application data"""
    if mode != 1:
        labels = model.neighbours.labels_
        candidate_cluster = model.predict_cluster(candidate)
        similar = model.X_train[labels == candidate_cluster]
        data = pd.DataFrame(similar, columns=X.columns)
    else:
        data = X
    n, bins, patches = plt.hist(
        data[variable], 50, density=False, facecolor="g", alpha=0.75
    )
    plt.axvline(
        candidate[variable][0],
        color="b",
        linestyle="dashed",
        linewidth=1,
        label="Candidate",
    )
    plt.axvline(
        data[variable].mean(),
        color="k",
        linestyle="dashed",
        linewidth=1,
        label="Variable mean",
    )
    plt.xlabel(variable)
    plt.ylabel("Value")
    plt.legend()
    plt.title("Histogram of " + variable)
    plt.grid(True)
    if mode == 1:
        variable = "global_" + variable
    else:
        variable = "similar_" + variable
    plt.savefig("./images/" + variable + ".png")
    plt.clf()
    return "./images/" + variable + ".png"


@hug.get("/get_data2", output=hug.output_format.image("png"))
@hug.local()
def graph_box(variable: hug.types.text, mode: hug.types.number, hug_timer=3):
    """Export graph candidate application data"""
    if mode != 1:
        labels = model.neighbours.labels_
        candidate_cluster = model.predict_cluster(candidate)
        similar = model.X_train[labels == candidate_cluster]
        data = pd.DataFrame(similar, columns=X.columns)
    else:
        data = X

    plt.boxplot(data[variable])
    plt.scatter(1, candidate[variable])
    plt.annotate("Candidate", (1, candidate[variable]))
    plt.xticks(ticks=[1], labels=[variable])
    plt.title("Boxplot of " + variable)

    if mode == 1:
        variable = "global_" + variable
    else:
        variable = "similar_" + variable
    plt.savefig("./images/box_" + variable + ".png")
    plt.clf()
    return "./images/box_" + variable + ".png"
