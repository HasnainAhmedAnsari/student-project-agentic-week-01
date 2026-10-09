
def validate_name(name):
    return isinstance(name, str) and bool(name.strip())


def validate_marks(marks):
    return isinstance(marks, (int, float)) and not isinstance(marks, bool) and 0 <= marks <= 100