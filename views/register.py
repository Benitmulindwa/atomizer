from flet import *

from flet import *


def Register(page):
    content = Column(
        controls=[
            Container(
                width=400,
                height=500,
                bgcolor="blue",
                content=Text("This the register page"),
            )
        ]
    )
    return content
