#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as te:
        import sys
        print("{}".format(te), file=sys.stderr)
        return False
    else:
        return True
