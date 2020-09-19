def Base_case_recursion(num, base):
    string = '0123456789ABCDEF'
    if num < base:
        return string[num]
    else:
        return Base_case_recursion(num//base, base) + string[num % base]


def Convert_digit_binary(num):
    c = '01'
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    else:
        return Convert_digit_binary(num//2) + c[num % 2]

print(Base_case_recursion(1453, 16))
print(Convert_digit_binary(10))
