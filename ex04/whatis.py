import sys


def whatis(a) -> None:
    """Print whether the integer a is odd or even."""
    if a % 2 == 0:
        print("I'm even.")
    else:
        print("I'm odd.")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AssertionError("exactly one argument is requiered")
        a = int(sys.argv[1])
        whatis(a)
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")
