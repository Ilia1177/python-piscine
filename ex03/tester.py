from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print("-- personal tests --")
NULL_not_found("0")
NULL_not_found("hello")
NULL_not_found(1.34)
NULL_not_found(True)
NULL_not_found("None")
NULL_not_found("nan")
NULL_not_found("NaN")
print(NULL_not_found("Brian"))
