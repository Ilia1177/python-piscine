import sys


def whatis(a) -> None:
    """Print whether the integer a is odd or even."""
    if a % 2 == 0:
        print("I'm even.")
    else:
        print("I'm odd.")


def main():
    try:
        if len(sys.argv) < 2:
            print("")
            return
        if len(sys.argv) > 2:
            raise AssertionError("More than on argument is provided")
        try:
            a = int(sys.argv[1])
        except ValueError:
            raise AssertionError("Argument is not an integer")
        whatis(a)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
