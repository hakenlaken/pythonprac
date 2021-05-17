from . import solve, fig


def main():
    a, b = map(float, input("Input a,b:").split())
    print(fig(solve(a, b)))


if __name__ == "__main__":
    main()
