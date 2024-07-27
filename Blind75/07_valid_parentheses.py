def isValid(s: str) -> bool:
    stack = []
    hm = {")": "(", "}": "{", "]": "["}
    for p in s:
        if p in hm:
            if stack and stack[-1] == hm[p]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p)

    return True if not stack else False


if __name__ == "__main__":
    s = "()[]{}"
    print(isValid(s))
