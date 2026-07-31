def evalRPN(tokens):
    stack = []
    ops = {"+", "-", "*", "/"}
    for t in tokens:
        if t in ops:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]

if __name__ == "__main__":
    print(evalRPN(["2","1","+","3","*"]))
