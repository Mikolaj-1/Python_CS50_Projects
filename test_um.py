from um import count

def test_for1():
    assert count("um?")==1
def test_for2():
    assert count("Um, thanks for the album.")==1
def test_for3():
    assert count("Um, thanks, um...")==2