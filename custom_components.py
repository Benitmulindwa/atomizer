from flet import *
from functools import partial


class LoginAndRegisterUI(UserControl):
    def __init__(self, page, fields_list: list, up_txt: str, func):
        super().__init__()
        self.page = page
        self.fields_list = fields_list
        self.up_txt = up_txt
        self.func = func

    def build(self):
        # print(self.custom_textfield("vagaga").controls[1].content)
        self.login_text = Container(
            content=Text(
                self.up_txt,
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
                    *[self.custom_textfield(i) for i in self.fields_list],
                    Container(
                        Text(
                            value="DO YOU HAVE AN ACCOUNT? "
                            if self.up_txt == "CREATE  AN  ACCOUNT"
                            else " DO NOT HAVE AN ACCOUNT? ",
                            font_family="lastica",
                            size=12,
                            spans=[
                                TextSpan(
                                    " Login"
                                    if self.up_txt == "CREATE  AN  ACCOUNT"
                                    else " CREATE",
                                    TextStyle(
                                        color="#d73cbe",
                                        font_family="lastica",
                                        size=12,
                                        weight=FontWeight.BOLD,
                                    ),
                                    on_click=self._go_to_login
                                    if self.up_txt == "CREATE  AN  ACCOUNT"
                                    else self._go_to_register,
                                ),
                            ],
                        ),
                        margin=margin.only(top=15),
                        padding=padding.only(left=10, right=10),
                    ),
                    Container(
                        Text(
                            "Create an account"
                            if self.up_txt == "CREATE  AN  ACCOUNT"
                            else "Login ",
                            weight=FontWeight.BOLD,
                            text_align="center",
                        ),
                        bgcolor="#8919db",
                        border_radius=5,
                        width=150 if self.up_txt == "CREATE  AN  ACCOUNT" else 100,
                        margin=margin.only(top=25, bottom=25),
                        padding=padding.only(bottom=4),
                        on_click=partial(self.func),
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
            # offset=transform.Offset(0, -2),
            # animate_offset=animation.Animation(1000),
        )
        self._container.margin = margin.only(top=60, bottom=100)

        return self._container

    def custom_textfield(self, name: str):
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
                        password=True if name == "Password:" else False,
                        can_reveal_password=True if name == "Password:" else False,
                        keyboard_type=KeyboardType.EMAIL
                        if name == "Email:"
                        else KeyboardType.TEXT,
                        enable_suggestions=True,
                    ),
                    padding=padding.only(left=10, right=10, top=0, bottom=15),
                ),
            ],
            expand=True,
        )

    def _go_to_login(self, e):
        return self.page.go("/")

    def _go_to_register(self, e):
        return self.page.go("/register")
