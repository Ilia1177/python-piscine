def NULL_not_found(object) -> int:
    if type(object) is type(None):
        print(f"Nothing: {object} <class '{type(object).__name__}'>")
        return 0
    # elif str(object) == "nan" and type(object).__name__ == "float":
    elif str(object) == "nan" and type(object) is float:
        print(f"Cheese: {object} <class '{type(object).__name__}'>")
        return 0
    # elif object == 0 and type(object) is int:
    elif object == 0 and type(object).__name__ != "bool":
        print(f"Zero: {object} <class '{type(object).__name__}'>")
        return 0
    elif object == "":
        print(f"Empty: {object} <class '{type(object).__name__}'>")
        return 0
    elif object is False:
        print(f"Fake: {object} <class '{type(object).__name__}'>")
        return 0
    else:
        print("Type not Found")
        return 1
