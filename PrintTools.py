def sPrint(text, delay= 0.03):
    import time
    for x in text:
        print(x, end="")
        time.sleep(delay)
    print()