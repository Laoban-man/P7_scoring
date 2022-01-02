# Dash components, html, and dash tables
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import Bootstrap components
import dash_bootstrap_components as dbc

# Import custom data.py
import data
import plotly.graph_objs as go

# Import data from data.py file
teams_df = data.teams
# Hardcoded list that contain era names and marks
era_list = data.era_list
era_marks = data.era_marks


# Main application menu
appMenu = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H4(style={"text-align": "center"}, children="xxx"),
                    xs={"size": "auto", "offset": 0},
                    sm={"size": "auto", "offset": 0},
                    md={"size": "auto", "offset": 3},
                    lg={"size": "auto", "offset": 0},
                    xl={"size": "auto", "offset": 0},
                ),
                dbc.Col(
                    dcc.Dropdown(
                        style={
                            "text-align": "center",
                            "font-size": "18px",
                            "width": "210px",
                        },
                        id="era-dropdown",
                        options=era_list,
                        value=era_list[0]["value"],
                        clearable=False,
                    ),
                    xs={"size": "auto", "offset": 0},
                    sm={"size": "auto", "offset": 0},
                    md={"size": "auto", "offset": 0},
                    lg={"size": "auto", "offset": 0},
                    xl={"size": "auto", "offset": 0},
                ),
                dbc.Col(
                    html.H4(
                        style={"text-align": "center", "justify-self": "right"},
                        children="xxx",
                    ),
                    xs={"size": "auto", "offset": 0},
                    sm={"size": "auto", "offset": 0},
                    md={"size": "auto", "offset": 3},
                    lg={"size": "auto", "offset": 0},
                    xl={"size": "auto", "offset": 1},
                ),
                dbc.Col(
                    dcc.Dropdown(
                        style={
                            "text-align": "center",
                            "font-size": "18px",
                            "width": "210px",
                        },
                        id="team-dropdown",
                        clearable=False,
                    ),
                    xs={"size": "auto", "offset": 0},
                    sm={"size": "auto", "offset": 0},
                    md={"size": "auto", "offset": 0},
                    lg={"size": "auto", "offset": 0},
                    xl={"size": "auto", "offset": 0},
                ),
            ],
            form=True,
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    style={"font-size": "16px", "opacity": "70%"},
                    children="""xxx """ """xxx.""",
                )
            )
        ),
    ],
    className="menu",
)
variableLayout1 = html.Div(
    [
        dcc.Dropdown(
            id="demo-dropdown1",
            options=[
                {"label": "APP_CODE_GENDER", "value": "APP_CODE_GENDER"},
                {"label": "APP_DAYS_BIRTH", "value": "APP_DAYS_BIRTH"},
                {"label": "APP_DAYS_EMPLOYED", "value": "APP_DAYS_EMPLOYED"},
                {"label": "APP_DAYS_ID_PUBLISH", "value": "APP_DAYS_ID_PUBLISH"},
            ],
            value="APP_CODE_GENDER",
        ),
        html.Div(id="dd-output-container1"),
        # html.Button("Plot", id="btn-nclicks-2", n_clicks=0),
        # html.Div(id="container-button-variable"),
    ]
)
variableLayout2 = html.Div(
    [
        dcc.Dropdown(
            id="demo-dropdown2",
            options=[
                {"label": "APP_CODE_GENDER", "value": "APP_CODE_GENDER"},
                {"label": "APP_DAYS_BIRTH", "value": "APP_DAYS_BIRTH"},
                {"label": "APP_DAYS_EMPLOYED", "value": "APP_DAYS_EMPLOYED"},
                {"label": "APP_DAYS_ID_PUBLISH", "value": "APP_DAYS_ID_PUBLISH"},
            ],
            value="APP_CODE_GENDER",
        ),
        html.Div(id="dd-output-container2"),
        # html.Button("Plot", id="btn-nclicks-2", n_clicks=0),
        # html.Div(id="container-button-variable"),
    ]
)

plotLayout1 = html.Div(
    [
        html.H4("\nVariable distribution"),
        dcc.Graph(
            id="interactive-image1",
            style={"width": "90vh", "height": "60vh"},
            figure={
                "layout": go.Layout(
                    # width = 800,
                    height=300,
                    xaxis={
                        "zeroline": False,
                        "showgrid": False,
                        "visible": False,
                        "color": "#FFFFFF",
                    },
                    yaxis={"showgrid": False, "zeroline": False, "visible": False},
                )
            },
        ),
        dcc.Graph(
            id="interactive-image3",
            style={"width": "90vh", "height": "60vh"},
            figure={
                "layout": go.Layout(
                    # width = 800,
                    height=300,
                    xaxis={
                        "zeroline": False,
                        "showgrid": False,
                        "visible": False,
                        "color": "#FFFFFF",
                    },
                    yaxis={"showgrid": False, "zeroline": False, "visible": False},
                )
            },
        ),
    ]
)
plotLayout2 = html.Div(
    [
        html.H4("\nVariable distribution"),
        dcc.Graph(
            id="interactive-image2",
            style={"width": "90vh", "height": "60vh"},
            figure={
                "layout": go.Layout(
                    # width = 800,
                    height=300,
                    xaxis={
                        "zeroline": False,
                        "showgrid": False,
                        "visible": False,
                        "color": "#FFFFFF",
                    },
                    yaxis={"showgrid": False, "zeroline": False, "visible": False},
                )
            },
        ),
        dcc.Graph(
            id="interactive-image4",
            style={"width": "90vh", "height": "60vh"},
            figure={
                "layout": go.Layout(
                    # width = 800,
                    height=300,
                    xaxis={
                        "zeroline": False,
                        "showgrid": False,
                        "visible": False,
                        "color": "#FFFFFF",
                    },
                    yaxis={"showgrid": False, "zeroline": False, "visible": False},
                )
            },
        ),
    ]
)

plotLayout3 = html.Div(
    [
        html.H4("\nLocal interpretation"),
        dcc.Graph(
            id="interactive-image6",
            style={"width": "90vh", "height": "60vh"},
            figure={
                "layout": go.Layout(
                    # width = 800,
                    height=300,
                    xaxis={
                        "zeroline": False,
                        "showgrid": False,
                        "visible": False,
                        "color": "#FFFFFF",
                    },
                    yaxis={"showgrid": False, "zeroline": False, "visible": False},
                )
            },
        ),
        html.H4("\nGlobal interpretation"),
        dcc.Graph(
            id="interactive-image7",
            style={"width": "90vh", "height": "60vh"},
            figure={
                "layout": go.Layout(
                    # width = 800,
                    height=300,
                    xaxis={
                        "zeroline": False,
                        "showgrid": False,
                        "visible": False,
                        "color": "#FFFFFF",
                    },
                    yaxis={"showgrid": False, "zeroline": False, "visible": False},
                )
            },
        ),
    ]
)

listLayout = html.Div(
    [
        html.H1("File Browser"),
        html.H2("Upload"),
        dcc.Upload(
            id="upload-data",
            children=html.Div(["Drag and drop or click to select a file to upload."]),
            style={
                "width": "100%",
                "height": "60px",
                "lineHeight": "60px",
                "borderWidth": "1px",
                "borderStyle": "dashed",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "10px",
            },
            multiple=True,
        ),
        html.H2("File List"),
        html.Ul(id="file-list"),
    ],
    style={"max-width": "500px"},
)

sendLayout = html.Div(
    [
        html.Button("Submit", id="btn-nclicks-1", n_clicks=0),
        html.Div(id="container-button-timestamp"),
    ]
)


predictbuttonLayout = html.Div(
    [
        html.Button("Evaluate", id="btn-nclicks-3", n_clicks=0),
        html.Div(id="container-button-predict"),
    ]
)

interpretbuttonLayout = html.Div(
    [
        html.Button("Interpret", id="btn-nclicks-4", n_clicks=0),
        html.Div(id="container-button-predict"),
    ]
)


applicationLayout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3(children="Application data"))),
        dbc.Row(
            dbc.Col(
                html.Div(id="team-data"),
                xs={"size": "auto", "offset": 0},
                sm={"size": "auto", "offset": 0},
                md={"size": 7, "offset": 0},
                lg={"size": "auto", "offset": 0},
                xl={"size": "auto", "offset": 0},
            ),
            justify="center",
        ),
    ],
    className="app-page",
)

explorationLayout1 = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dash_table.DataTable(
                    id="batterTable1",
                    style_as_list_view=True,
                    editable=False,
                    style_table={
                        "overflowY": "scroll",
                        "width": "100%",
                        "minWidth": "100%",
                    },
                    style_header={"backgroundColor": "#f8f5f0", "fontWeight": "bold"},
                    style_cell={"textAlign": "center", "padding": "8px"},
                ),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 10, "offset": 0},
                lg={"size": 10, "offset": 0},
                xl={"size": 10, "offset": 0},
            ),
            justify="center",
        ),
        dbc.Row(
            dbc.Col(
                html.H3(
                    style={"margin-top": "1%", "margin-bottom": "1%"},
                    children="Global Comparison",
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.H4(
                    style={"margin-top": "1%", "margin-bottom": "1%"},
                    children="Variable Analysis",
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    style={"font-size": "16px", "opacity": "70%"},
                    children="Select a variable to see its distribution across all clients and candidate position.",
                )
            )
        ),
    ],
    className="app-page",
)
explorationLayout2 = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dash_table.DataTable(
                    id="batterTable2",
                    style_as_list_view=True,
                    editable=False,
                    style_table={
                        "overflowY": "scroll",
                        "width": "100%",
                        "minWidth": "100%",
                    },
                    style_header={"backgroundColor": "#f8f5f0", "fontWeight": "bold"},
                    style_cell={"textAlign": "center", "padding": "8px"},
                ),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 10, "offset": 0},
                lg={"size": 10, "offset": 0},
                xl={"size": 10, "offset": 0},
            ),
            justify="center",
        ),
        dbc.Row(
            dbc.Col(
                html.H3(
                    style={"margin-top": "1%", "margin-bottom": "1%"},
                    children="Similar client comparison",
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.H4(
                    style={"margin-top": "1%", "margin-bottom": "1%"},
                    children="Variable Analysis",
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    style={"font-size": "16px", "opacity": "70%"},
                    children="Select a variable to see its distribution across similar clients and the candidate's position.",
                )
            )
        ),
    ],
    className="app-page",
)
scoringLayout = html.Div(
    dcc.Graph(id="potential"),
)

predictLayout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.H3(
                    style={"margin-bottom": "1%"},
                    children="Credit score evaluation result:",
                )
            )
        ),
    ],
    className="app-page",
)
