import os

import dash_bootstrap_components as dbc


app_name = os.getenv("DASH_APP_PATH", "/credit-scoring-tool")

# Navigation Bar fucntion
def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Data upload", href=f"{app_name}/application")),
            dbc.NavItem(
                dbc.NavLink("Data exploration", href=f"{app_name}/exploration")
            ),
            dbc.NavItem(dbc.NavLink("Creding scoring", href=f"{app_name}/predict")),
        ],
        brand="Home",
        brand_href=f"{app_name}",
        sticky="top",
        color="light",
        dark=False,
        expand="lg",
    )
    return navbar
