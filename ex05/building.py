import sys


def building(s):
    """Count characters, letters cases, punctuation, spaces and digits."""
    ponctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"
    total = sum(1 for c in s)
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    digit = sum(1 for c in s if c.isdigit())
    space = sum(1 for c in s if c.isspace())
    ponct = sum(1 for c in s if c in ponctuation)
    print(f"The text contains {total} characters")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{ponct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """Program to count characters in argument"""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Only one argument should be provided")
        elif len(sys.argv) == 1 or sys.argv[1] == "":
            print("What is the text to count?")
            s = sys.stdin.read()
            building(s)
        else:
            building(sys.argv[1])
    except AssertionError as e:
        print(f"Assertion error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as e:
        print(f"Error: {e}")
