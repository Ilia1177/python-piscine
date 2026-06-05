import sys


PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"


def building(s):
    """Count characters, letters cases, punctuation, spaces and digits."""
    total = sum(1 for c in s)
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    digit = sum(1 for c in s if c.isdigit())
    space = sum(1 for c in s if c.isspace())
    ponct = sum(1 for c in s if c in PUNCTUATION)
    print(f"The text contains {total} characters")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{ponct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    elif len(sys.argv) == 1:
        print("What is the text to count?")
        s = sys.stdin.read()
        building(s)
    else:
        building(sys.argv[1])


if __name__ == "__main__":
    main()
