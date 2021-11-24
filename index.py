import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
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
    upload_file,
)
import callbacks
from app import app
from app import srv as server


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
        return upload_file, listLayout, applicationLayout
    elif pathname.endswith("/exploration"):
        return explorationLayout
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
    location = "/download/{}".format(urlquote(filename))
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
        return [html.Li(file_download_link(filename)) for filename in files]


# Set layout to index function
app.layout = index()

# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
