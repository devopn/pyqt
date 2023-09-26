import string


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    error = "LengthError"


class LetterError(PasswordError):
    error = "LetterError"


class DigitError(PasswordError):
    error = "DigitError"


class SequenceError(PasswordError):
    error = "SequenceError"


def check_password(password):
    russian_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    russian_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    banned_combinations = [
        "qwe",
        "wer",
        "ert",
        "rty",
        "tyu",
        "yui",
        "uio",
        "iop",
        "asd",
        "sdf",
        "dfg",
        "fgh",
        "ghj",
        "hjk",
        "jkl",
        "zxc",
        "xcv",
        "cvb",
        "vbn",
        "bnm",
        "йцу",
        "цук",
        "уке",
        "кен",
        "енг",
        "нгш",
        "гшщ",
        "шщз",
        "щзх",
        "зхъ",
        "фыв",
        "ыва",
        "вап",
        "апр",
        "про",
        "рол",
        "олд",
        "лдж",
        "джэ",
        "жэё",
        "ячс",
        "чсм",
        "сми",
        "мит",
        "ить",
        "тьб",
        "ьбю",
        "123",
        "234",
        "345",
        "456",
        "567",
        "678",
        "789",
        "890",
    ]
    if len(password) <= 8:
        raise LengthError
    isDigit = False
    isLower = False
    isUpper = False

    for i in password:
        if (i in string.ascii_lowercase) or (i in russian_lower):
            isLower = True
        if (i in string.ascii_uppercase) or (i in russian_upper):
            isUpper = True
        if i in string.digits:
            isDigit = True

    if not (isLower and isUpper):
        raise LetterError

    if not isDigit:
        raise DigitError

    for i in banned_combinations:
        if i in password.lower():
            raise SequenceError

    return "ok"


while True:
    try:
        password = input()
        print(check_password(password))
        break

    except KeyboardInterrupt:
        print("Bye-Bye")
        break
    except (LengthError, DigitError, LetterError, SequenceError) as e:
        print(e.error)
