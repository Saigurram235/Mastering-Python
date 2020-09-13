import practic1
def infix_postfix(exp):
    s = practic1.Stack()
    prec = {'*': 3, '/': 3, '+':2, '-': 2, '(': 1}
    postfix_list = []
    split_exp = exp.split()
    for t in split_exp:
        if t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or t in "0123456789":
            postfix_list.append(t)
        elif t == '(':
            s.push(t)
        elif t == ')':
            top_token = s.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = s.pop()
        else:
            while (not s.is_empty()) and (prec[s.peek()] >= prec[t]):
                postfix_list.append(s.pop())
            s.push(t)
    while not s.is_empty():
        postfix_list.append(s.pop())
    return ' '.join(postfix_list)


print(infix_postfix("A * B + C * D"))
print(infix_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_postfix("( A + B ) * ( C + D )"))
print(infix_postfix("A + B * C"))
