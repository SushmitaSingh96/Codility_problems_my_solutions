def solution(S):
    if S == "":
        return 1
    stack = list()
    for i in S:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        elif i == ")" :
            if len(stack) == 0:
                return 0
            elif stack[-1] != "(":
                return 0
            else:
                stack.pop()
        elif i == "}":
            if len(stack) == 0:
                return 0
            elif stack[-1] != "{":
                return 0
            else:
                stack.pop()
        elif i == "]":
            if len(stack) == 0:
                return 0
            elif stack[-1] != "[":
                return 0
            else:
                stack.pop()
    if len(stack) == 0:
        return 1
    return 0
