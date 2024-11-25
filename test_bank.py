from bank import value

def test_hello():
    assert value("Hello") == 0
def test_hey():
    assert value("Hey") == 20
def test_dif():
    assert value("What's up") == 100
    assert value("What's good") == 100
