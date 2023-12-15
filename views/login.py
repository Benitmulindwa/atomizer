from flet import *
from custom_components import *


def Login(page):
    content = MyLoginpage(page, ["Email:", "Password:"], up_txt="LOGIN")
    return content
