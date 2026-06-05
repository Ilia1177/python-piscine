from ft_filter import ft_filter

def main() -> None:
    var = "I am a string."
    print(f"original filter: {list(filter(str.isupper, var))}")
    print(f"42 ft_filter   : {list(ft_filter(str.isupper, var))}")


if __name__ == "__main__":
    main()
