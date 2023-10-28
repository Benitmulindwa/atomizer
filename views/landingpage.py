from flet import *


def LandingPage(page):
    content = Column(
        controls=[
            Container(
                width=400,
                height=500,
                bgcolor="green",
                alignment=alignment.center,
                content=Text("This the landing page"),
            )
        ]
    )
    return content
