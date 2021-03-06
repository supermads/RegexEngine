# write your code here


def check_regex(first, second):
    if first == "$" and len(second) > 0:
        return False
    elif first == "$" and len(second) == 0:
        return True
    elif len(first) >= 2 and first[0] == "\\":
        if first[1] == second[0]:
            return check_regex(first[2:], second[1:])
        else:
            return False
    elif len(first) != 0:
        if len(first) > 1 and (first[1] == "?" or first[1] == "*" or first[1] == "+"):
            if first[0] == second[0] or first[0] == ".":
                if first[1] == "*" or first[1] == "+":
                    for i in range(1, (len(second))):
                        if first[0] != second[i]:
                            return check_regex(first[2:], second[i:])
                else:  
                    return check_regex(first[2:], second[1:])
            elif first[1] == "+":
                return False
            else:
                return check_regex(first[2:], second)
        elif len(second) != 0:
            if first[0] == "." or first[0] == second[0]:
                if first == second:
                    return True
                else:
                    return check_regex(first[1:], second[1:])
            else:
                return False
        else:
            return False
    else:
        return True


def main():
    first, second = input().split("|")
    if not first:
        return True
    if first[0] == "^":
        if check_regex(first[1], second[0]):
            first = first[2:]
            second = second[1:]
        else:
            return False
    if not first:
        return True
    while len(first) != 0 and len(second) != 0:
        if check_regex(first, second):
            return True
        else:
            second = second[1:]
    return False


print(main())
