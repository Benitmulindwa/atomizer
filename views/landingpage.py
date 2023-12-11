from flet import *

# ---------------------------------------------------------------------------------------------------------------#
## gradient Background ##
# ---------------------------------------------------------------------------------------------------------------#

# Container(
#     # expand=True,
#     height=800,
#     gradient=LinearGradient(
#         begin=alignment.center_left,
#         end=alignment.center_right,
#         colors=["#442063", "#1d3263"],
#     ),
#     alignment=alignment.center,
# ),

# ---------------------------------------------------------------------------------------------------------------#
##LOGO##
# ---------------------------------------------------------------------------------------------------------------#

# Row(
#                 controls=[
#                     Container(height=20, width=20, bgcolor="blue"),
#                     Text("ATOMIZER"),
#                 ],
#                 left=10,
#                 top=5,
#             ),

# ---------------------------------------------------------------------------------------------------------------#
landing_text = Container(
    expand=True,
    width=500,
    content=Text(
        "Your AI-Powered Science Problem - Solving Companion", expand=True, size=60
    ),
    alignment=alignment.center,
)

landing_text.padding = padding.only(left=20, top=30)
# ---------------------------------------------------------------------------------------------------------------#
################### GET STARTED BUTTOM #####################################
# ---------------------------------------------------------------------------------------------------------------#
getstarted = Container(
    width=600,
    height=35,
    bgcolor="#8919db",
    content=Text("GET STARTED", expand=True),
    alignment=alignment.center,
    border_radius=5,
)
getstarted.padding = padding.only(left=50)
# ---------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------#


def LandingPage(page):
    page.bgcolor = "#1d3263"
    return Column(
        horizontal_alignment=CrossAxisAlignment.CENTER,
        controls=[
            Row(
                controls=[
                    Container(height=20, width=20, bgcolor="blue"),
                    Text("ATOMIZER"),
                    Row(expand=True),
                    Container(
                        # expand=True,
                        content=Text("LOGIN", expand=True),
                        bgcolor="#8919db",
                        alignment=alignment.center,
                        border_radius=50,
                    ),
                ],
            ),
            Column(
                auto_scroll=True,
                expand=True,
                controls=[
                    Row(
                        # expand=True,
                        controls=[
                            landing_text,
                            Container(height=500, expand=True, bgcolor="red"),
                        ],
                    ),
                    getstarted,
                ],
            ),
        ],
    )
