def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("height and weight lists must have the same length")
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [b > limit for b in bmi]
