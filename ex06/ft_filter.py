def ft_filter(function, iterable) -> None:
    """Mimic the python's builtin function filter."""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
