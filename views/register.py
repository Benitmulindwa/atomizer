from flet import *

from custom_components import *


def Register(page):
    content = MyLoginpage(
        page, ["Username:", "Email:", "Password:"], up_txt="CREATE  AN  ACCOUNT"
    )
    return content
