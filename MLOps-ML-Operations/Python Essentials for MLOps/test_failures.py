from utils import str_to_bool

def test_str_to_int_fails():
    result = str_to_bool("14, 44")
    assert result == 14

def test_str_to_int_decimals():
    result = str_to_bool("14.44")
    assert result == 14

def test_str_to_int_with_integers():
    result = str_to_bool(10)
    assert result == 10