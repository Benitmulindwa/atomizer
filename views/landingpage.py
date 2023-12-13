from flet import *
from time import sleep


class Mylandingpage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        # self.text_size = 0
        self.text_size = int((self.page.width / 21))
        # self.page.width.update()
        # # print(self.text_size)

    def build(self):
        # self.page.update()

        self.logo = Container(height=30, width=30, bgcolor="blue")
        self.logo.margin = margin.only(left=10, top=20)

        self._atomizer = Container(
            content=Text(
                "ATOMIZER",
            ),
        )
        self._atomizer.margin = margin.only(top=20)

        self.landing_anim = Container(
            col={"sm": 4, "md": 6, "xl": 6},
            height=300,
            bgcolor="red",
        )
        self.landing_anim.margin = margin.only(right=20)
        # ---------------------------------------------------------------------------------------------------------------#
        ################### GET STARTED BUTTOM #####################################
        # ---------------------------------------------------------------------------------------------------------------#
        self.getstarted = Container(
            width=600,
            height=35,
            bgcolor="#8919db",
            content=Text("GET STARTED", expand=True),
            alignment=alignment.center,
            border_radius=5,
        )
        self.getstarted.margin = margin.only(left=20, right=20)

        # ---------------------------------------------------------------------------------------------------------------#
        #################### LOGIN BUTTON #########################
        # ---------------------------------------------------------------------------------------------------------------#
        self.login_bt = Container(
            width=100,
            height=20,
            content=Text("LOGIN"),
            bgcolor="#8919db",
            alignment=alignment.center,
            border_radius=50,
        )
        self.login_bt.margin = margin.only(right=20, top=20)

        # ---------------------------------------------------------------------------------------------------------------#
        #################### Landing Text #########################
        # ---------------------------------------------------------------------------------------------------------------#

        self.landing_text = Container(
            col={"sm": 4, "md": 6, "xl": 6},
            height=550,
            expand=True,
            content=Text(
                "Your AI-Powered Science Problem - Solving Companion",
                expand=True,
                size=self.text_size,
            ),
            alignment=alignment.center,
        )

        self.landing_text.margin = margin.only(left=20, top=30)

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
                                self.logo,
                                self._atomizer,
                                Row(expand=True),
                                self.login_bt,
                            ],
                            # top=20,
                        ),
                        Column(
                            controls=[
                                ResponsiveRow(
                                    vertical_alignment=CrossAxisAlignment.CENTER,
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        self.landing_text,
                                        self.landing_anim
                                        # landing_text,
                                    ],
                                ),
                                self.getstarted,
                            ],
                        ),
                    ]
                )
            ],
        )


# ---------------------------------------------------------------------------------------------------------------#


def LandingPage(page):
    content = Mylandingpage(page)

    return content
