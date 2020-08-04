# import random
#
#
# def find_level(level):
#     if level.lower() in ['easy', 'intermediate', 'hard']:
#         return level.lower()
#     else:
#         x = (input('Please select in This easy, intermediate, and hard: ')).lower()
#         return find_level(x)
#
#
# def find_Question(attemt):
#     if attemt.lower() in ['m', 'd', 'a', 's']:
#         return attemt.lower()
#     else:
#         x = (input('Please select in This multiplication:M, addition:A, subtraction:S, division:D : ')).lower()
#         return find_Question(x)
#
#
# # def sai(y, attempts, x):
# #     if y == 'M':
# #         for i in range(attempts):
# #             print(x, y)
# #     elif y == 'A':
# #         for i in range(attempts):
# #             print(x, y)
# #     elif y == 'S':
# #         for i in range(attempts):
# #             print(x, y)
# #     elif y == 'D':
# #         for i in range(attempts):
# #             print(x, y)
#
#
# def easy(y, attempts):
#     if y == 'M':
#         for i in range(attempts):
#             a = random.randint(1, 100)
#             b = random.randint(1, 100)
#             x = int(input("What's %d multiplication by %d?" %(a, b)))
#             g = a*b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'A':
#         for i in range(attempts):
#             a = random.randint(1, 100)
#             b = random.randint(1, 100)
#             x = int(input("What's %d addition by %d?" %(a, b)))
#             g = a+b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'S':
#         for i in range(attempts):
#             a = random.randint(1, 100)
#             b = random.randint(1, 100)
#             x = int(input("What's %d subtraction by %d?" %(a, b)))
#             g = a-b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'D':
#         for i in range(attempts):
#             a = random.randint(1, 100)
#             b = random.randint(1, 100)
#             x = int(input("What's %d division by %d?" %(a, b)))
#             g = a/b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#
#
# def inter(y, attempts):
#     if y == 'M':
#         for i in range(attempts):
#             a = random.randint(100, 1000)
#             b = random.randint(100, 1000)
#             x = int(input("What's %d multiplication by %d?" %(a, b)))
#             g = a*b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'A':
#         for i in range(attempts):
#             a = random.randint(100, 1000)
#             b = random.randint(100, 1000)
#             x = int(input("What's %d addition by %d?" %(a, b)))
#             g = a+b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'S':
#         for i in range(attempts):
#             a = random.randint(100, 1000)
#             b = random.randint(100, 1000)
#             x = int(input("What's %d subtraction by %d?" %(a, b)))
#             g = a-b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'D':
#         for i in range(attempts):
#             a = random.randint(100, 1000)
#             b = random.randint(100, 1000)
#             x = int(input("What's %d division by %d?" %(a, b)))
#             g = a/b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#
#
# def hard(y, attempts):
#     if y == 'M':
#         for i in range(attempts):
#             a = random.randint(1000, 1500)
#             b = random.randint(1000, 1500)
#             x = int(input("What's %d multiplication by %d?" %(a, b)))
#             g = a*b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'A':
#         for i in range(attempts):
#             a = random.randint(1000, 1500)
#             b = random.randint(1000, 1500)
#             x = int(input("What's %d addition by %d?" %(a, b)))
#             g = a+b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'S':
#         for i in range(attempts):
#             a = random.randint(1000, 1500)
#             b = random.randint(1000, 1500)
#             x = int(input("What's %d subtraction by %d?" %(a, b)))
#             g = a-b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#     elif y == 'D':
#         for i in range(attempts):
#             a = random.randint(1000, 1500)
#             b = random.randint(1000, 1500)
#             x = int(input("What's %d division by %d?" %(a, b)))
#             g = a/b
#             if g == x:
#                 print("That's right -- well done")
#             else:
#                 print('Wrong Answer')
#                 print('ouput:', g)
#
# def Continue(c):
#     if c.upper() == 'C':
#         level = input('Choose level (easy, intermediate, and hard): ')
#         x = find_level(level).capitalize()
#
#         attempts = int(input('Please give us the number of question you want to attempt: '))
#
#         question = input('Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ')
#         y = find_Question(question).upper()
#
#         if x == 'Easy':
#             easy(y, attempts)
#             c = input('Continue or exit (Continue:C, Exit: E) : ')
#             Continue(c)
#         elif x == 'Intermediate':
#             inter(y, attempts)
#             c = input('Continue or exit (Continue:C, Exit: E) : ')
#             Continue(c)
#         elif x == 'Hard':
#             hard(y, attempts)
#             c = input('Continue or exit (Continue:C, Exit: E) : ')
#             Continue(c)
#     else:
#         SystemExit
#
#
# level = input('Choose level (easy, intermediate, and hard): ')
# x = find_level(level).capitalize()
#
# attempts = int(input('Please give us the number of question you want to attempt: '))
#
# question = input('Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ')
# y = find_Question(question).upper()
#
# if x == 'Easy':
#     easy(y, attempts)
#     c = input('Continue or exit (Continue:C, Exit: E) : ')
#     Continue(c)
# elif x == 'Intermediate':
#     inter(y, attempts)
#     c = input('Continue or exit (Continue:C, Exit: E) : ')
#     Continue(c)
# elif x == 'Hard':
#     hard(y, attempts)
#     c = input('Continue or exit (Continue:C, Exit: E) : ')
#     Continue(c)

# 2nd


# def exp(a, b):
#     if b == 0:
#         print('The %d raised to the power of %d is : ' % (a, b), 1)
#     elif b < 0:
#         return 1/(a * exp(a, b + 1))
#     else:
#         return a * exp(a, b - 1)
#
#
# # x = int(input('Find the power to the value: '))
# # n = int(input('How much power you raised to x : '))
# print(exp(2, 3))

# def fast_exp(x, n):
#     if n == 0:
#         return 1
#     elif n % 2 == 0:
#         return fast_exp(x*x, n/2)
#     else:
#         return x * fast_exp(x, n-1)
# print(fast_exp(3, 2))

# def exp(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * exp(x, n - 1)
#
# print(exp(3, 2))


# mylist = [["john", 1, "a"], ["larry", 0, "b"]]
# mylist.sort(key=lambda x: x[1])
# print(mylist)
#
# from operator import itemgetter
# mylist = [["john", 1, "a"], ["larry", 0, "b"]]
# mylist.sort(key=itemgetter(1))
# print(mylist)