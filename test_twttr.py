from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"

def test_shorten_only_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("") == ""

def test_shorten_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("PyThOn") == "PyThn"

def test_shorten_with_numbers():
    assert shorten("CS50x") == "CS50x"
    assert shorten("0123456789") == "0123456789"

def test_shorten_with_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("!@#$%^&*()") == "!@#$%^&*()"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_single_character():
    assert shorten("a") == ""
    assert shorten("Z") == "Z"

if __name__ == "__main__":
    test_shorten_no_vowels()
    test_shorten_only_vowels()
    test_shorten_mixed_case()
    test_shorten_with_numbers()
    test_shorten_with_punctuation()
    test_shorten_empty_string()
    test_shorten_single_character()
