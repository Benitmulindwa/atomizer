from flet import *
from time import sleep
from custom_components import *

from authentication import _login_user


class Mylandingpage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.text_size = int((self.page.width / 21))
        self.login_content = LoginAndRegisterUI(
            self.page, ["Email:", "Password:"], up_txt="LOGIN", func=self._login
        )

    def build(self):
        self.logo = Container(height=30, width=30, bgcolor="blue")
        self.logo.margin = margin.only(left=10, top=20)

        self._atomizer = Container(
            content=Text("ATOMIZER", font_family="lastica"),
        )
        self._atomizer.margin = margin.only(top=20)

        self.login_form = Container(
            self.login_content,
            col={"md": 6, "xl": 6},
            height=650,
            expand=True,
            alignment=alignment.center,
        )
        # self.landing_anim.margin = margin.only(left=10)
        self.login_form.padding = padding.only(left=50, right=50)
        # ---------------------------------------------------------------------------------------------------------------#
        ################### GET STARTED BUTTOM #####################################
        # ---------------------------------------------------------------------------------------------------------------#
        self.getstarted = Container(
            width=600,
            expand=True,
            bgcolor="#8919db",
            content=Text("GET STARTED", expand=True, font_family="lastica"),
            alignment=alignment.center,
            border_radius=5,
            on_click=self._go_to_register,
        )
        self.getstarted.margin = margin.only(left=20, right=20, top=0)

        # ---------------------------------------------------------------------------------------------------------------#
        #################### LOGIN BUTTON #########################
        # ---------------------------------------------------------------------------------------------------------------#
        self.login_bt = Container(
            width=160,
            height=25,
            content=Text("GET STARTED", font_family="lastica"),
            bgcolor="#8919db",
            alignment=alignment.center,
            border_radius=50,
            on_click=self._go_to_register,
        )
        self.login_bt.margin = margin.only(right=20, top=20)
        self.login_bt.padding = padding.only(top=4)

        # ---------------------------------------------------------------------------------------------------------------#
        #################### Landing Text #########################
        # ---------------------------------------------------------------------------------------------------------------#

        self.landing_text = Container(
            col={"md": 6, "xl": 6},
            width=650,
            expand=True,
            content=Text(
                "Your  AI-Powered  Science  Problem - Solving Companion",
                expand=True,
                size=45,
                font_family="lastica",
                weight=FontWeight.BOLD,
            ),
            alignment=alignment.center,
            on_click=self.animate_text,
        )

        self.landing_text.margin = margin.only(left=30, top=0, bottom=50)
        self.landing_text.padding = padding.only(right=0, top=10)

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
                ResponsiveRow(
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.landing_text,
                        self.login_form,
                    ],
                ),
            ],
        )

    def _login(self, e):
        loggedin = _login_user(self.login_form)
        self.login_form.content.controls[0].content.controls[1].controls[
            1
        ].content.value = ""
        self.login_form.content.controls[0].content.controls[2].controls[
            1
        ].content.value = ""
        self.login_form.content.controls[0].update()
        if loggedin == True:
            self.page.go("/chat")

    def animate_text(self, e):
        word_list = []
        for word in self.landing_text.content.value:
            word_list.append(word)
            self.landing_text.content.value = "".join(word_list)
            self.landing_text.content.update()
            sleep(0.08)

    ## GO TO REGISTER ##
    def _go_to_register(self, e):
        return self.page.go("/register")


# ---------------------------------------------------------------------------------------------------------------#


def LandingPage(page):
    content = Mylandingpage(page)

    return Container(
        content=Column(
            [
                content,
            ],
            expand=True,
            scroll=ScrollMode.AUTO,
        ),
        alignment=alignment.center,
        height=800,
        expand=True,
        gradient=LinearGradient(
            begin=alignment.center_left,
            end=alignment.center_right,
            colors=["#001f3f", "#191970"],
        ),
    )
