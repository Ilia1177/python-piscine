import sys


def count(iterable):
    """count iterable"""
    count = 0
    for c in iterable:
        count += 1
    return count


def is_upper(c):
    """check is upper char"""
    return 'A' <= c <= 'Z'


def is_lower(c):
    """check is lower char"""
    return 'a' <= c <= 'z'


def is_digit(c):
    """check is digit char"""
    return '0' <= c <= '9'


def is_space(c):
    """check is space char"""
    return c in (' ', '\t', '\n', '\r', '\v', '\f')


def building(s):
    """Count characters, letters cases, punctuation, spaces and digits."""
    ponctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"
    total = count(1 for c in s)
    upper = count(1 for c in s if is_upper(c))
    lower = count(1 for c in s if is_lower(c))
    digit = count(1 for c in s if is_digit(c))
    space = count(1 for c in s if is_space(c))
    ponct = count(1 for c in s if c in ponctuation)
    print(f"The text contains {total} characters")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{ponct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """Program to count characters in argument"""
    try:
        if count(sys.argv) > 2:
            raise AssertionError("Only one argument should be provided")
        elif count(sys.argv) == 1 or sys.argv[1] == "":
            print("What is the text to count?")
            s = sys.stdin.read()
            building(s)
        else:
            building(sys.argv[1])
    except AssertionError as e:
        print(f"Assertion error: {e}")
    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
