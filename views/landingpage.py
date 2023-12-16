from flet import *
from time import sleep
from custom_components import *


class Mylandingpage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.text_size = int((self.page.width / 21))
        self.content = MyLoginpage(self.page, ["Email:", "Password:"], up_txt="LOGIN")

    def build(self):
        self.logo = Container(height=30, width=30, bgcolor="blue")
        self.logo.margin = margin.only(left=10, top=20)

        self._atomizer = Container(
            content=Text("ATOMIZER", font_family="lastica"),
        )
        self._atomizer.margin = margin.only(top=20)

        self.landing_anim = Container(
            col={"md": 6, "xl": 6},
            height=200,
            bgcolor="red",
        )
        self.landing_anim.margin = margin.only(left=20, right=20)
        # ---------------------------------------------------------------------------------------------------------------#
        ################### GET STARTED BUTTOM #####################################
        # ---------------------------------------------------------------------------------------------------------------#
        self.getstarted = Container(
            width=600,
            height=35,
            expand=True,
            bgcolor="#8919db",
            content=Text("GET STARTED", expand=True, font_family="lastica"),
            alignment=alignment.center,
            border_radius=5,
            on_click=self._go_to_login,
        )
        self.getstarted.margin = margin.only(left=20, right=20, top=0)

        # ---------------------------------------------------------------------------------------------------------------#
        #################### LOGIN BUTTON #########################
        # ---------------------------------------------------------------------------------------------------------------#
        self.login_bt = Container(
            width=100,
            height=25,
            content=Text("LOGIN", font_family="lastica"),
            bgcolor="#8919db",
            alignment=alignment.center,
            border_radius=50,
            on_click=self._go_to_login,
        )
        self.login_bt.margin = margin.only(right=20, top=20)
        self.login_bt.padding = padding.only(top=4)

        # ---------------------------------------------------------------------------------------------------------------#
        #################### Landing Text #########################
        # ---------------------------------------------------------------------------------------------------------------#

        self.landing_text = Container(
            col={"md": 6, "xl": 6},
            height=550,
            expand=True,
            content=Text(
                "Your  AI-Powered  Science  Problem - Solving Companion",
                expand=True,
                size=45,
                font_family="lastica",
                weight=FontWeight.BOLD,
            ),
            alignment=alignment.center,
            # on_hover=self.animate_text,
        )

        self.landing_text.margin = margin.only(left=20, top=50)

        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            auto_scroll=True,
            controls=[
                Row(
                    controls=[
                        self.logo,
                        self._atomizer,
                        Row(expand=True),
                        self.login_bt,
                    ],
                    # top=20,
                ),
                Row(
                    # vertical_alignment=CrossAxisAlignment.CENTER,
                    # alignment=MainAxisAlignment.CENTER,
                    controls=[self.landing_text, self.content],
                ),
                # self.getstarted,
            ],
        )

    def animate_text(self, e):
        word_list = []
        for word in self.landing_text.content.value:
            word_list.append(word)
            self.landing_text.content.value = "".join(word_list)
            self.landing_text.content.update()
            sleep(0.08)

    ## GO TO LOGIN ##
    def _go_to_login(self, e):
        return self.page.go("/login")


# ---------------------------------------------------------------------------------------------------------------#


def LandingPage(page):
    content = Mylandingpage(page)
    login_content = MyLoginpage(page, ["Email:", "Password:"], up_txt="LOGIN")
    login_container = Container(
        login_content,
        expand=True,
    )
    # login_container.margin = margin.only(left=800)

    return Container(
        content=Column(
            [
                content,
                # login_container,
            ],
        ),
        alignment=alignment.center,
        height=800,
        expand=True,
        gradient=LinearGradient(
            begin=alignment.center_left,
            end=alignment.center_right,
            colors=["#1d3263", "#442063"],
        ),
    )
