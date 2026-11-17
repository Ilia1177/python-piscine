from ft_filter import ft_filter

def main() -> None:
    var = "I am a string."
    print("original filter:")
    print(f"{list(filter(str.isupper, var))}")
    print(f"__doc__: {filter.__doc__}")
    print("ft_filter:")
    print(f"{list(ft_filter(str.isupper, var))}")
    print(f"__doc__: {ft_filter.__doc__}")


if __name__ == "__main__":
    main()
