def is_balanced(L):
    stack = []
    for i in range(0,len(L)):
        if L[i] == '{' or L[i] == '(' or L[i] == '[':
            stack.append(L[i])
        elif L[i] == '}' and stack.pop() != '{':
            return False
        elif L[i] == ')' and stack.pop() != '(':
            return False
        elif L[i] == ']' and stack.pop() != '[':
            return False
    if len(stack) == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    L = raw_input()
    print is_balanced(L)