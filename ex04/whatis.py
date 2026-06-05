import sys


def whatis(a) -> None:
    if a % 2 == 0:
        print("I'm even.")
    else:
        print("I'm odd.")


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        a = int(sys.argv[1])
        whatis(a)
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")
