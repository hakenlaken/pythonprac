import pyfiglet
import gettext
import os
import locale

gettext.install("solve", os.path.dirname(__file__))


def solve(a:float, b: float):
    if a == 0:
        return None
    return -b / a


def fig(res) -> str:
    if locale.getlocale()[0] == "ru_RU":
        style = pyfiglet.Figlet(font="banner")
    else:
        style = pyfiglet.Figlet()
    if res is None:
        return style.renderText(_("NO ROOTS"))
    else:
        return style.renderText(_("Root: %f") % (res))

