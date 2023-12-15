from flet import Container

from views.landingpage import LandingPage
from views.login import Login
from views.register import Register

# from views.chat import Chat


class Route:
    def __init__(self, page):
        self.page = page
        self.routes = {
            "/": LandingPage(page),
            "/login": Login(page),
            "/register": Register(page),
            # "/chat": Chat(page),
        }
        self.body = Container(content=self.routes["/"], expand=True)

    def change_route(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()
