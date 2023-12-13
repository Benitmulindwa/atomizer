from views.Routing import Route
from flet import *
from time import sleep


def main(page: Page):
    page.theme_mode = "dark"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 0
    page.auto_scroll = True

    myroute = Route(page)
    page.on_route_change = myroute.change_route
    page.add(myroute.body)
    page.go("/")
    page.update()


if __name__ == "__main__":
    app(target=main)
