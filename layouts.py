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

# # Menu slider used, NOT independent, MUST be used with main menu
# menuSlider = html.Div(
#     [
#         dbc.Row(
#             dbc.Col(
#                 dcc.RangeSlider(
#                     id="era-slider",
#                     min=1903,
#                     max=teams_df["year"].max(),
#                     marks=era_marks,
#                     tooltip={"always_visible": False, "placement": "bottom"},
#                 )
#             )
#         ),
#         dbc.Row(
#             dbc.Col(
#                 html.P(
#                     style={"font-size": "16px", "opacity": "70%"},
#                     children="Adjust slider to desired range.",
#                 )
#             )
#         ),
#     ],
#     className="era-slider",
# )


# Layout for Team Analysis page
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
        ### Graphs of Historical Team statistics ###
        dbc.Row(dbc.Col(html.H3(children="Application data"))),
        # Bar Chart of Wins and Losses
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="wl-bar", config={"displayModeBar": False}),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 12, "offset": 0},
                lg={"size": 12, "offset": 0},
            )
        ),
    ],
    className="app-page",
)


# # Player menu used to select players after era and team are set
# explorationMenu = html.Div(
#     [
#         dbc.Row(dbc.Col(html.H3(children="Player Profile and Statistics"))),
#         dbc.Row(
#             dbc.Col(
#                 html.P(
#                     style={"font-size": "16px", "opacity": "70%"},
#                     children="Available players are updated based on team selection.",
#                 )
#             )
#         ),
#         dbc.Row(
#             [
#                 dbc.Row(
#                     dbc.Col(
#                         html.H4(
#                             style={"text-align": "center"}, children="Select Player:"
#                         ),
#                         xs={"size": "auto", "offset": 0},
#                         sm={"size": "auto", "offset": 0},
#                         md={"size": "auto", "offset": 0},
#                         lg={"size": "auto", "offset": 0},
#                         xl={"size": "auto", "offset": 0},
#                     )
#                 ),
#                 dbc.Row(
#                     dbc.Col(
#                         dcc.Dropdown(
#                             style={
#                                 "margin-left": "2%",
#                                 "text-align": "center",
#                                 "font-size": "18px",
#                                 "width": "218px",
#                             },
#                             id="player-dropdown",
#                             clearable=False,
#                         ),
#                         xs={"size": "auto", "offset": 0},
#                         sm={"size": "auto", "offset": 0},
#                         md={"size": "auto", "offset": 0},
#                         lg={"size": "auto", "offset": 0},
#                         xl={"size": "auto", "offset": 0},
#                     )
#                 ),
#             ],
#             no_gutters=True,
#         ),
#         html.Br(),
#         dbc.Row(
#             dbc.Col(
#                 dash_table.DataTable(
#                     id="playerProfile",
#                     style_as_list_view=True,
#                     editable=False,
#                     style_table={
#                         "overflowY": "scroll",
#                         "width": "100%",
#                         "minWidth": "100%",
#                     },
#                     style_header={"backgroundColor": "#f8f5f0", "fontWeight": "bold"},
#                     style_cell={"textAlign": "center", "padding": "8px"},
#                 ),
#                 xs={"size": "auto", "offset": 0},
#                 sm={"size": "auto", "offset": 0},
#                 md={"size": 8, "offset": 0},
#                 lg={"size": "auto", "offset": 0},
#                 xl={"size": "auto", "offset": 0},
#             ),
#             justify="center",
#         ),
#         html.Br(),
#     ],
#     className="app-page",
# )


# Batting statistics
explorationLayout = html.Div(
    [
        # Batting datatable
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
                    children="Player Analysis",
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    style={"font-size": "16px", "opacity": "70%"},
                    children="Some statistics where not tracked until the 1950s, graphs may not always reflect certain plots.",
                )
            )
        ),
        dbc.Row(
            [
                # Line/Bar Chart of On-Base Percentage, features; H BB HBP SF
                dbc.Col(
                    dcc.Graph(id="obp-line", config={"displayModeBar": False}),
                    xs={"size": 12, "offset": 0},
                    sm={"size": 12, "offset": 0},
                    md={"size": 12, "offset": 0},
                    lg={"size": 6, "offset": 0},
                ),
                # Line/Bar Chart of Slugging Average, features; 2B 3B HR
                dbc.Col(
                    dcc.Graph(id="slg-line", config={"displayModeBar": False}),
                    xs={"size": 12, "offset": 0},
                    sm={"size": 12, "offset": 0},
                    md={"size": 12, "offset": 0},
                    lg={"size": 6, "offset": 0},
                ),
            ],
            no_gutters=True,
        ),
        # Line Chart of OPS, Features; OBP SLG
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="ops-line", config={"displayModeBar": False}),
                xs={"size": 12, "offset": 0},
                sm={"size": 12, "offset": 0},
                md={"size": 12, "offset": 0},
                lg={"size": 12, "offset": 0},
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
