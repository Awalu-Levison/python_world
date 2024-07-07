#!/usr/bin/python3i


def safe_print_integer(value):
    """print integers only
    if not, control the error with an exception
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
