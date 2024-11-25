from working import convert

def test_zero():
    assert convert("12 AM to 6 PM")=="0:00 to 18:00"
    assert convert("8 AM to 6 PM")=="8:00 to 18:00"
    assert convert("11 AM to 10 PM")=="11:00 to 22:00"

def test_False():
    assert convert("12:60 AM to 6 PM")==False
    assert convert("3 AM to 13 PM")==False
    assert convert("11:-1 AM to 16 PM")==False

def test_half():
    assert convert("12:30 AM to 6 PM")=="0:30 to 18:00"
    assert convert("8 AM to 6:12 PM")=="8:00 to 18:12"
    assert convert("11:25 AM to 10:32 PM")=="11:25 to 22:32"
