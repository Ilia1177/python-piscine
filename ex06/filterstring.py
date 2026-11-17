import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "wrong number of arguments."
        assert sys.argv[2].lstrip('-').isdigit(), "Bad arguments"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    n = int(sys.argv[2])
    s = sys.argv[1]
    words = [w for w in s.split()]
    result = list(ft_filter(lambda word: len(word) > n, words))
    print(result)


if __name__ == "__main__":
    main()
