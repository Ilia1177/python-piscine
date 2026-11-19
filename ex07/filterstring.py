import sys


def main():
    """Program that return words in arg 1 longer than arg 2"""
    try:
        assert len(sys.argv) == 3, "wrong number of arguments."
        assert sys.argv[2].lstrip('-').isdigit(), "Bad arguments"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    n = int(sys.argv[2])
    s = sys.argv[1]
    words = [w for w in s.split()]
    result = [w for w in words if len(w) > n]
    print(result)


if __name__ == "__main__":
    main()
