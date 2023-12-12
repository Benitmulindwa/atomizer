from flet import *
from time import sleep

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
getstarted.margin = margin.only(left=20)

# ---------------------------------------------------------------------------------------------------------------#
#################### LOGIN BUTTON #########################
# ---------------------------------------------------------------------------------------------------------------#
login_bt = Container(
    # expand=True,
    width=100,
    height=20,
    content=Text("LOGIN"),
    bgcolor="#8919db",
    alignment=alignment.center,
    border_radius=50,
)

# ---------------------------------------------------------------------------------------------------------------#
#################### Landing Text #########################
# ---------------------------------------------------------------------------------------------------------------#

landing_text = Container(
    expand=True,
    height=500,
    content=Text(
        "Your AI-Powered Science Problem - Solving Companion", expand=True, size=60
    ),
    alignment=alignment.center,
)

# landing_text.content.value = ""
# for word in landing_text.content.value.split(" "):
#     landing_text.content.value = "".join(word)
#     landing_text.content.update()
#     sleep(0.008)

landing_text.padding = padding.only(left=20, top=30)

# ---------------------------------------------------------------------------------------------------------------#


def LandingPage(page):
    return Column(
        horizontal_alignment=CrossAxisAlignment.CENTER,
        auto_scroll=True,
        controls=[
            Stack(
                controls=[
                    Container(
                        expand=True,
                        height=800,
                        gradient=LinearGradient(
                            begin=alignment.center_left,
                            end=alignment.center_right,
                            colors=["#442063", "#1d3263"],
                        ),
                        alignment=alignment.center,
                    ),
                    Row(
                        controls=[
                            Container(height=30, width=30, bgcolor="blue"),
                            Text("ATOMIZER"),
                            Row(expand=True),
                            login_bt,
                        ],
                        # top=10,
                    ),
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    Row(
                                        controls=[
                                            # Container(
                                            #     expand=True,
                                            #     width=500,
                                            #     content=Text(
                                            #         "Your AI-Powered Science Problem - Solving Companion",
                                            #         # expand=True,
                                            #         size=60,
                                            #     ),
                                            #     alignment=alignment.center,
                                            # )
                                            # landing_text,
                                            Container(
                                                expand=True, height=500, bgcolor="blue"
                                            ),
                                            Text("gfgfgfgfytrytrhhgjhjuyuy"),
                                        ],
                                    ),
                                    # landing_text,
                                    Container(height=300, expand=True, bgcolor="red"),
                                ]
                            ),
                            getstarted,
                        ],
                    ),
                ]
            )
        ],
    )
