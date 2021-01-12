My Solution:

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
    pass

StackOverflow Solution:

def solution(S):

    matches, stack = dict(['()', '[]', '{}']), []

    for i in S:
        if i in matches.values():
            if stack and matches[stack[-1]] == i:
                stack.pop()
            else:
                return 0
        else:
            stack.append(i)

    return int(not stack)