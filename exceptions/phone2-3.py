import string


class FormatError(Exception):
    error = "FormatError"


class UnderlineError(FormatError):
    error = "UnderlineError"


class CountryError(Exception):
    error = "StartError"


class NumAmountError(Exception):
    error = "NumAmountError"


class BracketError(FormatError):
    error = "BracketError"


class DefError(FormatError):
    error = "DefError"


class OperatorError(Exception):
    error = "OperatorError"


def except_found(num: str):
    # Brakets close check
    for i in range(1, len(num) - 1):
        if (num[i] == ")") and (num[i - 1] == ")"):
            raise BracketError

    for i in range(1, len(num) - 1):
        if (num[i] == "(") and (num[i - 1] == "("):
            raise BracketError

    brackets_open = "("
    brackets_closed = ")"
    stack = []
    for i in num:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                raise BracketError
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                raise BracketError
    if num.count("(") != num.count(")"):
        raise BracketError
    for i in range(1, len(num) - 1):
        if (num[i] == "-") and (num[i - 1] == "-"):
            raise DefError


    num = num.replace("(", "")
    num = num.replace(")", "")

    for i in num:
        if i in string.ascii_letters:
            raise FormatError
        bad = string.punctuation
        bad = bad.replace(")", "!")
        bad = bad.replace("(", "!")
        bad = bad.replace("-", "!")
        bad = bad.replace("+", "!")
        if i in bad:
            # print(bad)
            raise FormatError
    num = num.replace(" ", "")
    notChanged = True
    num = num.replace("\t", "")
    if (num[0] == "-") or (num[-1] == "-"):
        raise UnderlineError
    num = num.replace("-", "")
    if len([i for i in num if i.isdigit()]) != 10:
        raise NumAmountError
    if num.startswith("+7"):
        num = num.replace("+7", "", 1)
        notChanged = False
    if num.startswith("8"):
        num = num.replace("8", "", 1)
        notChanged = False
    if num.startswith("+359"):
        num = num.replace("+359", "", 1)
        notChanged = False
    if num.startswith("+55"):
        num = num.replace("+55", "", 1)
        notChanged = False
    if num.startswith("+1"):
        num = num.replace("+1", "", 1)
        notChanged = False

    if notChanged:
        raise CountryError

    known_operators = list()
    known_operators.extend(range(910, 920))
    known_operators.extend(range(980, 990))
    known_operators.extend(range(920, 940))
    known_operators.extend(range(902, 907))
    known_operators.extend(range(960, 970))
    # print(known_operators)
    if int(num[:3]) not in known_operators:
        raise OperatorError
    return f"+7{num[0:3]}{num[3:6]}{num[6:8]}{num[8:10]}"


number = input()
try:
    print(except_found(number))
except NumAmountError:
    print("неверное количество цифр")

except FormatError as e:
    print("неверный формат")
    # print(e.error)

except OperatorError:
    print("не определяется оператор сотовой связи")

except CountryError:
    print("не определяется код страны")
