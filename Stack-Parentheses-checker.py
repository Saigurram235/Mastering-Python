import practic1


def par_checker(string_brakets):
    b = True
    s = practic1.Stack()
    i = 0
    while i < len(string_brakets) and b:
        sy = string_brakets[i]
        if sy == '(':
            s.push(sy)
        else:
            if s.is_empty():
                b = False
            else:
                s.pop()
        i = i + 1
    if b and s.is_empty():
        return 'The Input Parentheses is Balanced'
    else:
        return 'The Input Parenthesis is Not Balanced'

print(par_checker('((()()()))'))
print(par_checker('()()()(((('))
print(par_checker('((()))'))
