from flet import *


def animate_cont(page, route: str):
    if route == "/login":
        page.controls[0].content.controls[0].content.controls[0].controls[
            0
        ].offset = transform.Offset(0, 0)
        page.controls[0].content.controls[0].content.controls[0].controls[0].update()
    else:
        page.go(route)
        page.update()
