from source.response_utils.random import setNextInt, randint


def test_random():
    value = randint(1, 2)
    assert value > 0 and value < 3

    setNextInt(0)
    assert randint(1, 2) == 0
