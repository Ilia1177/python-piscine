def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")
    if len({len(row) for row in family}) > 1:
        raise ValueError("All rows must have the same length")
    rows = len(family)
    cols = len(family[0]) if rows > 0 else 0
    print(f"My shape is : ({rows}, {cols})")
    new_list = family[start:end]
    rows = len(new_list)
    cols = len(new_list[0]) if rows > 0 else 0
    print(f"My new shape is : ({rows}, {cols})")
    return new_list
