from typing import Any


def NULL_not_found(object: Any) -> int:
    if object is None:
        print(f"Nothing: {object} <class '{type(object).__name__}'>")
        return 0
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} <class '{type(object).__name__}'>")
        return 0
    elif type(object) is int and object == 0:
        print(f"Zero: {object} <class '{type(object).__name__}'>")
        return 0
    elif object == "":
        print(f"Empty: <class '{type(object).__name__}'>")
        return 0
    elif object is False:
        print(f"Fake: {object} <class '{type(object).__name__}'>")
        return 0
    else:
        print("Type not Found")
        return 1
