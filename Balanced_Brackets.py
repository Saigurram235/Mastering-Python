import practic1


def balanced_bracket(symbol):
    b = True
    i = 0
    s = practic1.Stack()
    while i < len(symbol) and b:
        sy = symbol[i]
        if sy in '{[(':
          s.push(sy)
        else:
            if s.is_empty():
                b = False
            else:
                top = s.pop()
                if not matches(top, sy):
                    b =False
        i = i + 1

    if b and s.is_empty():
        return 'It is Balanced'
    else:
        return 'It is not Balanced'
def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)

print(balanced_bracket('[{()}][][][{()()}]'))
print(balanced_bracket('[][(){}{]'))
print(balanced_bracket('{{([][])}()}'))
