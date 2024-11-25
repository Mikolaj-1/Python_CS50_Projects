from  numb3rs import validate

def test_true():
    assert validate("12.12.12.12")==True
    assert validate("32.53.122.92")==True
    assert validate("255.255.255.0")==True

def test_notInt():
    assert validate("cat")==False
    assert validate("ds.ds.24.52")==False
    assert validate("dsffdsg")==False

def test_wrongVal():
    assert validate("262.24.12.95")==False
    assert validate("426.2454.1245.1334")==False
    assert validate("-23.45.43.122")==False
