from flet import *

from views.Routing import Route


def main(page: Page):
    page.theme_mode = "dark"

    myroute = Route(page)
    page.on_route_change = myroute.change_route
    page.add(myroute.body)
    page.go("/")


if __name__ == "__main__":
    app(target=main)
