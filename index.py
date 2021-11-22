# import dash-core, dash-html, dash io, bootstrap
import os

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Dash Bootstrap components
import dash_bootstrap_components as dbc

# Navbar, layouts, custom callbacks
from navbar import Navbar
from layouts import (
    appMenu,
    menuSlider,
    explorationMenu,
    applicationLayout,
    explorationLayout,
    predictLayout,
)
import callbacks

# Import app
from app import app

# Import server for deployment
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
# Declair function  that connects other pages with content to container
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
        return appMenu, menuSlider, applicationLayout
    elif pathname.endswith("/exploration"):
        return appMenu, menuSlider, explorationMenu, explorationLayout
    elif pathname.endswith("/predict"):
        return appMenu, menuSlider, explorationMenu, predictLayout
    else:
        return "ERROR 404: Page not found!"


# Main index function that will call and return all layout variables
def index():
    layout = html.Div([nav, container])
    return layout


# Set layout to index function
app.layout = index()

# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
