from stack import * 


def check_brackets(brackets):
    s = Stack()
    closing = ["}", "]", ")"]
    opening = ["{", "[", "("]
    for b in brackets:
        if b in opening:
            s.append(b)
        else:
            b = s.pop()
            if 


