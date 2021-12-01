# Dash components, html, and dash tables
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import Bootstrap components
import dash_bootstrap_components as dbc

# Import custom data.py
import data

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
variableLayout = html.Div(
    [
        dcc.Dropdown(
            id="demo-dropdown",
            options=[
                {"label": "sepal length (cm)", "value": "sepal length (cm)"},
                {"label": "sepal width (cm)", "value": "sepal width (cm)"},
                {"label": "petal length (cm)", "value": "petal length (cm)"},
                {"label": "petal width (cm)", "value": "petal width (cm)"},
            ],
            value="sepal length (cm)",
        ),
        html.Div(id="dd-output-container"),
        # html.Button("Plot", id="btn-nclicks-2", n_clicks=0),
        # html.Div(id="container-button-variable"),
    ]
)

plotLayout = html.Div(
    [
        html.H3("\nVariable distribution"),
        dcc.Graph(id="interactive-image", style={"width": "90vh", "height": "90vh"}),
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


applicationLayout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3(children="Application data"))),
        # Display Championship titles in datatable
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

explorationLayout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dash_table.DataTable(
                    id="batterTable",
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
                    children="Variable Analysis",
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    style={"font-size": "16px", "opacity": "70%"},
                    children="Select a variable to see distribution and candidate position.",
                )
            )
        ),
    ],
    className="app-page",
)


# Feilding Statistics
predictLayout = html.Div(
    [
        dbc.Row(dbc.Col(html.H3(style={"margin-bottom": "1%"}, children="A"))),
        # Feilding Datatable
        dbc.Row(
            dbc.Col(
                dash_table.DataTable(
                    id="fieldTable",
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
                md={"size": 8, "offset": 0},
                lg={"size": 8, "offset": 0},
                xl={"size": 8, "offset": 0},
            ),
            justify="center",
        ),
        html.Br(),
        dbc.Row(dbc.Col(html.H3(style={"margin-bottom": "1%"}, children="B"))),
        dbc.Row(
            dbc.Col(
                html.Div(id="pitch-data"),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 10, "offset": 0},
                lg={"size": 10, "offset": 0},
                xl={"size": 10, "offset": 0},
            ),
            justify="center",
        ),
        html.Br(),
        dbc.Row(dbc.Col(html.H3(children="Player C"))),
        dbc.Row(dbc.Col(html.H4(children="Pitching Performance"))),
    ],
    className="app-page",
)
