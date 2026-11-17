import sys


def main():
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    try:
        assert len(sys.argv) == 2, "wrong number of arguments."
        assert all(c.upper() in NESTED_MORSE for c in sys.argv[1]), "argument must be alphanumeric"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    s = sys.argv[1]
    result = [NESTED_MORSE[c.upper()] for c in s]
    return print(" ".join(result))


if __name__ == "__main__":
    main()
