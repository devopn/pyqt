def except_found(num: str):
    num = num.replace(" ", "")
    num = num.replace("\t", "")
    if (num[0] == "-") or (num[-1] == "-"):
        return False
    if not (num.startswith("+7") or num.startswith("8")):
        return False

    if num.startswith("+7"):
        num = num.replace("+7", "", 1)
    if num.startswith("8"):
        num = num.replace("8", "", 1)

    if len([i for i in num if i.isdigit()]) != 10:
        return False

    # Brakets close check
    for i in range(1, len(num) - 1):
        if (num[i] == ")") and (num[i - 1] == ")"):
            return False
        
    for i in range(1, len(num) - 1):
        if (num[i] == "(") and (num[i - 1] == "("):
            return False

    brackets_open = "("
    brackets_closed = ")"
    stack = []
    for i in num:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                return False
    if num.count("(") != num.count(")"):
        return False
    for i in range(1, len(num) - 1):
        if (num[i] == "-") and (num[i - 1] == "-"):
            return False

    num = num.replace("-", "")
    num = num.replace("(", "")
    num = num.replace(")", "")
    return f"+7{num[0:3]}{num[3:6]}{num[6:8]}{num[8:10]}"


number = input()
if except_found(number):
    print(except_found(number))
else:
    print("error")
