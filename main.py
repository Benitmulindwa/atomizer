from views.Routing import Route
from flet import *
from time import sleep


def main(page: Page):
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 0
    page.fonts = {"lastica": "fonts/FontsFree-Net-Lastica.ttf"}
    page.auto_scroll = True
    myroute = Route(page)
    page.on_route_change = myroute.change_route
    page.add(myroute.body)
    page.go("/")
    page.update()
    # if page.route == "/login":
    #     page.controls[0].content.controls[0].content.controls[0].controls[
    #         0
    #     ].offset = transform.Offset(0, 0)
    #     page.controls[0].content.controls[0].content.controls[0].controls[0].update()


if __name__ == "__main__":
    app(target=main)
