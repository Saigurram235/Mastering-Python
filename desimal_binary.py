import practic1

def binary(num):
    rem_stack = practic1.Stack()
    while num > 0:
        rem = num % 2
        rem_stack.push(rem)
        num = num//2

    binary_string = ''
    while not rem_stack.is_empty():
        binary_string = binary_string + str(rem_stack.pop())
    return binary_string

print(binary(45))
# for i in range(1,10):
#     print(binary(i))