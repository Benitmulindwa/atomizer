from flet import *


def LandingPage(page):
    content = Stack(
        # expand=True,
        controls=[
            Container(
                # expand=True,
                height=800,
                gradient=LinearGradient(
                    begin=alignment.center_left,
                    end=alignment.center_right,
                    colors=["#442063", "#1d3263"],
                ),
                # padding=padding.all(0),
                alignment=alignment.center,
            ),
            Text("ATOMIZER", left=10, top=5),
            Column(
                # expand=True,
                controls=[
                    Container(
                        expand=True,
                        width=500,
                        # height=300,
                        bgcolor="red",
                        content=Text(
                            "Your AI-Powered Science Problem- Solving Companion",
                            size=50,
                        ),
                    ),
                ],
                left=20,
                top=50,
            ),
        ],
    )
    return content
