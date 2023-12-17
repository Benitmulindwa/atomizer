from flet import *
from custom_components import *


def Register(page):
    content = LoginAndRegisterUI(
        page, ["Username:", "Email:", "Password:"], up_txt="CREATE  AN  ACCOUNT"
    )
    return Container(
        content=Stack(
            [
                content,
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
