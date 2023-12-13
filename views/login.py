from flet import *

from flet import *


class MyLoginpage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        self._login_text = Container(
            content=Text(
                "LOGIN",
                bgcolor="blue",
                font_family="lastica",
                weight=FontWeight.BOLD,
            )
        )
        # self._login_text.alignment = alignment.center
        self._container = Container(
            width=420,
            height=500,
            # bgcolor="transparent",
            border=border.all(2, "white"),
            opacity=0.3,
            alignment=alignment.center,
        )
        self._container.margin = margin.only(top=100)
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
                        [
                            self._login_text,
                        ],
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
                colors=["#442063", "#1d3263"],
            ),
        )


def Login(page):
    content = MyLoginpage(page)
    return content
