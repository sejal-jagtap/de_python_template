from hello import say_hello, add, subtract


def test_say_hello():
    assert (
        say_hello("Sejal")
        == "Hello, Sejal, welcome to Data Engineering Systems (IDS 706)!"
    )


def test_add():
    assert add(6, 2) == 8
    assert add(6, 2) == 8


def test_subtract():
    assert subtract(6, 3) == 3
    assert subtract(0, 4) == -4
