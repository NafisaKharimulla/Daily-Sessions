from validator import validate, normalize
def test_valid_input():
    result, reasons = validate("This is a normal profile description")
    assert result == "VALID"
def test_email_detection():
    result, reasons = validate("contact me at test@gmail.com")
    assert result == "INVALID"
def test_phone_detection():
    result, reasons = validate("my number is 9876543210")
    assert result == "INVALID"
def test_url_detection():
    result, reasons = validate("visit http://example.com")
    assert result == "INVALID"
def test_normalize_function():
    text = "hello     world"
    assert normalize(text) == "hello world"
