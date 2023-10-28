from flet import *

from flet import *


def Login(page):
    content = Column(
        controls=[
            Container(
                width=400,
                height=500,
                content=Text("This the login page"),
                alignment=alignment.center,
            )
        ],
    )
    return content
