from flet import *
from custom_components import *
from authentication import _register_user


def Register(page):
    def _register(e):
        _register_user(content)
        content.controls[0].content.controls[1].controls[1].content.value = ""
        content.controls[0].content.controls[2].controls[1].content.value = ""
        content.controls[0].content.controls[3].controls[1].content.value = ""
        content.controls[0].update()

    content = LoginAndRegisterUI(
        page,
        ["Username:", "Email:", "Password:"],
        up_txt="CREATE  AN  ACCOUNT",
        func=_register,
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
