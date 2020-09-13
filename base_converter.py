import practic1

def binary(num, base):
    digits = "0123456789ABCDEF"
    rem_stack = practic1.Stack()
    while num > 0:
        rem = num % base
        rem_stack.push(rem)
        num = num//base

    binary_string = ''
    while not rem_stack.is_empty():
        binary_string = binary_string + digits[rem_stack.pop()]
    return binary_string

print(binary(25, 2))
print(binary(25, 16))
print(binary(25, 8))
for i in range(1,10):
    print(binary(i, 2))