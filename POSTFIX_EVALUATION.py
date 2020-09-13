import practic1

def post_evaluation(exp):
    exp_split = exp.split()
    s = practic1.Stack()
    for t in exp_split:
        if t in "0123456789":
            s.push(int(t))
        else:
            o1 = int(s.pop())
            o2 = int(s.pop())
            result = do_math(t, o2, o1)
            s.push(result)
    return int(s.pop())

def do_math(o, a, b):
    if o == '*':
        return a * b
    elif o == '/':
       return a/b
    elif o == '+':
        return a+ b
    elif o == '-':
        return a-b
    else:
        return 'wrong'

print(post_evaluation('7 8 + 3 2 + /'))