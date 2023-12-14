from flet import *

from flet import *


class MyLoginpage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        self.login_text = Container(
            content=Text(
                "CREATE  AN  ACCOUNT",
                font_family="lastica",
                weight=FontWeight.BOLD,
                text_align="center",
                size=15,
            ),
        )
        self.login_text.margin = margin.only(top=20, bottom=20)

        self._container = Container(
            Column(
                [
                    self.login_text,
                    self.custom_textfield("Username:"),
                    self.custom_textfield("Email:"),
                    self.custom_textfield("Password:", True),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            width=420,
            height=500,
            bgcolor="transparent",
            border=border.all(2, "white"),
            # opacity=0.3,
        )
        self._container.margin = margin.only(top=100)
        # self._container.padding = padding.only(top=10)
        return Container(
            content=Stack(
                [
                    Column(
                        controls=[
                            self._container,
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    Column(
                        [],
                        alignment=MainAxisAlignment.CENTER,
                        # horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                ],
            ),
            alignment=alignment.center,
            height=800,
            gradient=LinearGradient(
                begin=alignment.center_left,
                end=alignment.center_right,
                colors=["#1d3263", "#d73cb"],
            ),
        )

    def custom_textfield(self, name, password_state: bool = False):
        return Column(
            [
                Container(
                    Text(name, font_family="lastica"),
                    padding=padding.only(left=10, right=10, top=15),
                ),
                Container(
                    TextField(
                        bgcolor="white",
                        height=25,
                        text_style=TextStyle(color="black"),
                        border_radius=5,
                        border_color="white",
                        border=border.all(0.5, "white"),
                        cursor_color="#1d3263",
                        cursor_height=15,
                        password=password_state,
                        can_reveal_password=password_state,
                    ),
                    padding=padding.only(left=10, right=10, top=5),
                ),
            ]
        )


def Login(page):
    content = MyLoginpage(page)
    return content
