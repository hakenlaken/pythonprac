import pyfiglet


def solve(a: float, b: float):
    if a == 0:
        return None
    else:
        return -b / a


def fig(res) -> str:
    f = pyfiglet.Figlet()
    if res is None:
        return f.renderText("NO ROOTS")
    return f.renderText(f"Root: {res:.5f}")
