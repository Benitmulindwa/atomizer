from views.Routing import Route
from flet import *


def main(page: Page):
    page.title = "Atomizer"
    # page.window_frameless = True
    page.theme_mode = "system"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 0
    page.fonts = {"lastica": "fonts/FontsFree-Net-Lastica.ttf"}
    myroute = Route(page)
    page.on_route_change = myroute.change_route

    page.update()
    page.add(myroute.body)
    page.go("/")


if __name__ == "__main__":
    app(target=main)
