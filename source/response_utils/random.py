from random import randint as _randint

nextInt = None


def randint(a: int, b: int) -> int:
    global nextInt
    if nextInt is not None:
        value = nextInt
        nextInt = None
        return value
    return _randint(a, b)


def setNextInt(a: int) -> None:
    global nextInt
    nextInt = a
