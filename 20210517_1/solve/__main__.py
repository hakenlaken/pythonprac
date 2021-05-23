from . import solve, fig
import gettext
import os

gettext.install("solve", os.path.dirname(__file__))


a, b = map(float, input(_("Input a b: ")).split())
print(fig(solve(a, b)))

