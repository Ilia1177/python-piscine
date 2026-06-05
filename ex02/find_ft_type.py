def all_thing_is_obj(object) -> int:
    if type(object) is str:
        print(f"{object} is in the kitchen : {type(object)}")
    elif type(object) is int:
        print(f"Type not found")
    else:
        print(f"{type(object).__name__} : {type(object)}")
    return 42
