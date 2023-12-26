from flet import *
from custom_components import *
from authentication import _register_user


def Register(page):
    def _register(e):
        reg_status = _register_user(register_form)
        register_form.controls[0].content.controls[1].controls[1].content.value = ""
        register_form.controls[0].content.controls[2].controls[1].content.value = ""
        register_form.controls[0].content.controls[3].controls[1].content.value = ""
        register_form.controls[0].update()
        if reg_status == True:
            page.go("/chat")

    register_form = LoginAndRegisterUI(
        page,
        ["Username:", "Email:", "Password:"],
        up_txt="CREATE  AN  ACCOUNT",
        func=_register,
    )

    return Container(
        content=Stack(
            [
                register_form,
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
