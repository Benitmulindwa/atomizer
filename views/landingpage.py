from flet import *
from time import sleep

# ---------------------------------------------------------------------------------------------------------------#
################## Responsivity ###############
# ---------------------------------------------------------------------------------------------------------------#
# def resize(page,control):
#     if page.width>
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
getstarted.margin = margin.only(left=20, right=20)

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
    col={"sm": 4, "md": 4, "xl": 6},
    height=550,
    expand=True,
    content=Text(
        "Your AI-Powered Science Problem - Solving Companion", expand=True, size=60
    ),
    alignment=alignment.center,
)

landing_text.margin = margin.only(left=20, top=30)

# ---------------------------------------------------------------------------------------------------------------#


def LandingPage(page):
    content = Column(
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
                            ResponsiveRow(
                                vertical_alignment=CrossAxisAlignment.CENTER,
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    landing_text,
                                    Container(
                                        col={"sm": 2, "md": 4, "xl": 6},
                                        height=300,
                                        bgcolor="red",
                                    ),
                                    # landing_text,
                                ],
                            ),
                            getstarted,
                        ],
                    ),
                ]
            )
        ],
    )
    if 565 < page.width < 1190:
        landing_text.content.size = 30
        content.update()

    return content
