from plates import is_valid

def test_0():
    assert is_valid("CS05")==False
    assert is_valid("SSN052")==False

def test_nums():
    assert is_valid("522CS")==False
    assert is_valid("VA62CW")==False

def test_symbol():
    assert is_valid("CS1.6")==False
    assert is_valid("PI3.14")==False

def test_true():
    assert is_valid("CS50")==True
    assert is_valid("NDA63")==True
    assert is_valid("FAST")==True

def test_length():
    assert is_valid("CSNDSKAD")==False
    assert is_valid("D")==False

def test_alf():
    assert is_valid("NW62")==True
    assert is_valid("5CSN")==False