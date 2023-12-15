from flet import *


class MyLoginpage(UserControl):
    def __init__(self, page, name_list: list):
        super().__init__()
        self.page = page
        self.name_list = name_list

    def build(self):
        # print(self.custom_textfield("vagaga").controls[1].content)
        self.login_text = Container(
            content=Text(
                "CREATE  AN  ACCOUNT",
                font_family="lastica",
                weight=FontWeight.BOLD,
                text_align="center",
                size=15,
            ),
            expand=True,
        )
        self.login_text.margin = margin.only(top=40, bottom=20)

        self._container = Container(
            Column(
                [
                    self.login_text,
                    self.custom_textfield("Username:"),
                    self.custom_textfield("Email:"),
                    self.custom_textfield("Password:", True),
                    Container(
                        Text(
                            value="DO YOU HAVE AN ACCOUNT?",
                            font_family="lastica",
                            size=12,
                            # expand=True,
                            spans=[
                                TextSpan(
                                    " Login",
                                    TextStyle(
                                        color="#d73cbe",
                                        font_family="lastica",
                                        size=12,
                                        weight=FontWeight.BOLD,
                                    ),
                                    on_click=self._go_to_login,
                                ),
                            ],
                        ),
                        margin=margin.only(top=15),
                    ),
                    Container(
                        Text(
                            "Create an account",
                            weight=FontWeight.BOLD,
                            text_align="center",
                        ),
                        bgcolor="#8919db",
                        border_radius=5,
                        width=150,
                        margin=margin.only(top=25, bottom=25),
                        padding=padding.only(bottom=4),
                    ),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            width=420,
            expand=True,
            bgcolor="transparent",
            border=border.all(2, "white"),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color="#d73cbe",
                offset=Offset(0, 0),
                blur_style=ShadowBlurStyle.OUTER,
            ),
            # offset=transform.Offset(-2, 0),
            # animate_offset=animation.Animation(1000),
        )
        self._container.margin = margin.only(top=60, bottom=100)

        return Container(
            content=Stack(
                [
                    self._container,
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

    def custom_textfield(self, name, password_state: bool = False):
        return Column(
            controls=[
                Container(
                    Text(name, font_family="lastica"),
                    padding=padding.only(left=10, right=10, top=15, bottom=0),
                ),
                Container(
                    TextField(
                        bgcolor="white",
                        # expand=True,
                        height=25,
                        text_style=TextStyle(color="#8919db", weight=FontWeight.W_500),
                        content_padding=padding.only(top=4, left=5),
                        border_radius=5,
                        border_color="white",
                        border=border.all(0.5, "white"),
                        cursor_color="#1d3263",
                        cursor_height=22,
                        password=password_state,
                        can_reveal_password=password_state,
                    ),
                    padding=padding.only(left=10, right=10, top=0, bottom=15),
                ),
            ],
            expand=True,
        )

    def _go_to_login(self, e):
        return self.page.go("/login")
