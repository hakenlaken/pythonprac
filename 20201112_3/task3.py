while True:
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(input())
    except Exception:
        print("Invalid input")
        continue
    A = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
    if A > 0:
        print(f"{A:.{2}f}")
        break
    else:
        print("Not a triangle")
