from seasons import birth 

def test_true():
    assert birth("1999-01-01")=="thirteen million, two hundred and twenty thousand, six hundred and forty"

def test_false():
    assert birth("1 January 1999")=="Invalid date"