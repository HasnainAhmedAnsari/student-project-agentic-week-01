from student_app.utils.validation import validate_name, validate_marks


def test_valid_name():
    assert validate_name("Ali") is True


def test_empty_name():
    assert validate_name("") is False


def test_whitespace_name():
    assert validate_name("   ") is False


def test_valid_marks():
    assert validate_marks(85) is True


def test_zero_marks():
    assert validate_marks(0) is True


def test_hundred_marks():
    assert validate_marks(100) is True


def test_negative_marks():
    assert validate_marks(-10) is False


def test_marks_above_limit():
    assert validate_marks(150) is False