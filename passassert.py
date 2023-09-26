import string


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
    assert len(password) > 8
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
    assert isDigit
    assert isLower and isUpper

    for i in banned_combinations:
        assert i not in password.lower()

    print("ok")


psswd = input()
try:
    check_password(psswd)
except AssertionError:
    print("error")
