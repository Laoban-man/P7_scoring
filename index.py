import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from dash import callback_context
import dash_reusable_components as drc
import dash_bootstrap_components as dbc
from navbar import Navbar
from layouts import (
    appMenu,
    # menuSlider,
    # explorationMenu,
    listLayout,
    applicationLayout,
    explorationLayout,
    predictLayout,
    sendLayout,
    variableLayout,
    plotLayout,
)
import callbacks
from app import app
from app import srv as server
import base64
import urlquote
import requests
import pandas as pd
from flask import Flask, send_from_directory
import json
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import time

UPLOAD_DIRECTORY = "./uploaded_data"

app_name = os.getenv("DASH_APP_PATH", "/credit-scoring-tool")

# Layout variables, navbar, header, content, and container
nav = Navbar()

header = dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.H2(children="Credit scoring tool"),
                html.H3(children="Evaluating credit applications"),
            ]
        )
    ),
    className="banner",
)

content = html.Div([dcc.Location(id="url"), html.Div(id="page-content")])

container = dbc.Container([header, content])


@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


# Menu callback, set and return
# Declare function  that connects other pages with content to container
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname in [app_name, app_name + "/"]:
        return html.Div(
            [
                dcc.Markdown(
                    """
            ### The objective
            This tool provides the means for users to evaluate credit applications while understanding how the applicant compares to
            other applications based on the information provided.

            ### The Analysis
            Once applicant data is entered, it is possible to explore how they compare to collected data and understand the possible
            result of the prediction available in the credit scoring tool.

            ### The Data
            Home Credit provides this applicant data in an effort to develop more inclusive credit lending practices. In order to
            develop new algorithms to detect whether an credit application represents a significant risk, data available consists
            of current application details, past credit applications, credit card payments and balances, and installments.
        """
                )
            ],
            className="home",
        )
    elif pathname.endswith("/application"):
        return listLayout, sendLayout
    elif pathname.endswith("/exploration"):
        return explorationLayout, variableLayout, plotLayout
    elif pathname.endswith("/predict"):
        return predictLayout
    else:
        return "ERROR 404: Page not found!"


# Main index function that will call and return all layout variables
def index():
    layout = html.Div([nav, container])
    return layout


def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    # input_data = {"data": list(pd.read_csv("candidate.csv"))}
    # requests.get("http://localhost:8000/post_data", params=input_data)
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote.quote(filename))
    return html.A(filename, href=location)


@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [filename for filename in files]


@app.callback(
    Output("container-button-timestamp", "children"),
    Input("btn-nclicks-1", "n_clicks"),
)
def send_file(btn1):
    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    if "btn-nclicks-1" in changed_id:
        try:
            input_data = pd.read_csv("./uploaded_data/candidate.csv")
            input_data = {
                "columns": ",".join([a for a in input_data.columns]),
                "values": ",".join([str(a) for a in input_data.iloc[0, :]]),
            }
            input_data = json.dumps(input_data)
            response = requests.get(
                "http://localhost:8000/post_data", params=input_data
            )
            with open("log.txt", "wb") as f:
                f.write(response.content)
                f.close()
        except:
            with open("log.txt", "wb") as f:
                f.write("failed to send file\n")
                f.close()


@app.callback(
    Output("dd-output-container", "children"), Input("demo-dropdown", "value")
)
def update_output(value):
    try:
        input_data = {
            "variable": value,
        }
        # input_data = json.dumps(input_data)
        response = requests.get("http://localhost:8000/get_data", params=input_data)
        file = open("./downloaded_images/" + value + ".png", "wb")
        file.write(response.content)
        file.close()
        with open("log.txt", "wb") as f:
            f.write(response.content)
            f.close()
        # update_graph(str("./downloaded_images/" + value + ".png"))
    except:
        with open("log.txt", "wb") as f:
            f.write(b"failed to get variable\n")
            f.close()

    return


@app.callback(Output("interactive-image", "figure"), Input("demo-dropdown", "value"))
def update_graph(value):
    time.sleep(1)
    im_pil = Image.open("./downloaded_images/" + value + ".png")
    fig = px.imshow(im_pil)
    return fig


# @app.callback(
#      Output("container-button-variable", "children"),
#      Input("btn-nclicks-2", "n_clicks"),
# )
# def plot_variable(btn1):
#     changed_id = [p["prop_id"] for p in callback_context.triggered][0]
#     if "btn-nclicks-2" in changed_id:
#          try:
#              xx
#          except:
#              with open("log.txt", "wb") as f:
#                  f.write("failed")
#                  f.close()


# Set layout to index function
app.layout = index()

# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
