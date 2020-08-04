import math
import random
import numpy as np
import datetime
import time
import re

print(1)

# Numpy

x = math.exp(5*7+6)
print(x)

x = random.randrange(100)
print(x)

x = [random.randint(1, 6) for _ in range(10)]
print(x)

y = ['Python', 'Hadoop', 'DataScience', 'Stats']
x = random.choice(y)
print(x)

a = [25, 35 , 65, 55, 65]
b = np.array(a)
print(type(b))
print(b)
print(b*9/5+32)

for c in a:
    x = c*9/5+32
    print(x)

a = np.arange(1,10)
print(a)

a = np.arange(1,100,2)
print(a)

print(np.linspace(1,10))

A = np.array([[3, 4, 10],
            [4, 5, 6],
            [7, 8, 9],
            [58, 6, 9]])
print(A)
print(A.ndim)
print(np.shape(A))
A.shape = (3, 4)
print(A)
print(np.shape(A))

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s = A[2:6]
s[0] = 25
s[1] = 23
print(A)
print(s)

# e = np.ones((2, 3))
# print(e)
# f = np.ones((3,4), dttype=int)
# print(f)

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s = A.copy()
s[0] = 25
s[1] = 23
print(A)
print(s)

a = np.array([1, 2, 3, 4, 5, 6])
b = a[1:4]
b[0] = 200
print(a[1])

x = np.array([[0, 0, 1],[0, 1, 0],[1, 0, 0]])
y = ([3.65, 1.55, 3.42])
s = np.linalg.solve(x,y)
print(s)

x = np.array([[0, 0, 1],[0, 1, 0],[1, 1, 0]])
y = ([3.65, 1.55, 3.42])
s = np.linalg.solve(x,y)
print(s)

# datetime

print(datetime.datetime(1998,8,26,20,35))

print(datetime.datetime.today())
print(datetime.datetime.now())

d1 = datetime.datetime(1998,8,26,20,35)
d2 = datetime.datetime.today()

print(d2-d1)
print((d2-d1).days)
print((d2-d1).seconds)
print((d2-d1).total_seconds())

print(d1.strftime("%d/%m/%y"))

print(d1.strftime("%d/%m/%Y"))

print(d1.strftime("%A %d %B %Y"))

dt1 = datetime.datetime.strptime('30/07/2016 16:30', "%d/%m/%Y %H:%M")
print(dt1)

print((d2-dt1).days)
type(dt1)

e = d2 - datetime.timedelta(days=5)
q = e.strftime("%A %d %B %Y")
print(e)
print(q)

e = d2 + datetime.timedelta(days=5)
q = e.strftime("%A %d %B %Y")
print(e)
print(q)

e = time.time()
print(datetime.datetime.fromtimestamp(e))

print(time.mktime(d1.timetuple()))


# Regular Expression

# re.math()
# re.search()
# re.sub()
# re.compile()
# findall()

# Return the Match object
print(re.search('ab', 'Hear is an absolute string abababababab ab'))
print(re.search('xy', 'Hear is an absolute string abababababab ab'))


r = re.search('ab', 'Hear is an absolute string abababababab ab')
print(r.group())
print(r.start())
print(r.end())
print(r.span())

m = re.match(r"(..)+", "edureka")
print(m.group(1))

# (..)+ -> It will match any two consecutive characters. Hence there were three matches found 'edureka'
# Math1 : ed Math2: ur Math3: ek
#  a was left because it was not in pair
#  group(1) return only last match

e = 'sai@gmail.com, hsa@gmail.com, dsss@gmail.com, gafsfsf@yahoo.com'
print(re.findall(r'[\w\.-]+@gmail[\w\.-]+', e))

# search is used for single string
print(re.search(r'[\w\.-]+@gmail[\w\.-]+', e))

e = 'sai@gmail.com, hsa@gmail.com, dsss@gmail.com, gafsfsf@yahoo.com'
print(re.sub('gmail', 'yahoo', e))

p = re.compile('ab')
m = p.search('abbreviated')
print(m)
print(p)
print(m.group())

# Oops


class Acc:
    pass


class demo:
    def exp(self):
        return 0


x = Acc()
print(x)
ob = demo()
print(ob.exp())


class Edurecka():
    def __init__(self):
        self.__pri = "I am Private"
        self._pro = "I am Protected"
        self.pub = "I am Public"


ob = Edurecka()
print(ob.pub)
print(ob._pro)
# print(str(ob._Edurecka__pri()))


# Static Method

class Edureka:
    def static(a):
        print(a)


Edureka.static('This is a static method')


# Constructor

class Edureka:
    def __init__(self, name):
        self.name = name


ob = Edureka('Discover')
print(ob.name)

# Destructor


class Edureka:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('Del the')


ob = Edureka('pytyhon')
ob2 = ob

del ob
del ob2

# Further of oops

# Encapsulation : Dividing the code into a public interface, and a private implementation of that interface.

class ed:
    def __init__(self, c):
        self.c = c

    def sc(self, c):
        self.c = c

    def gc(self):
        return self.c


ob = ed('python')
print(ob.gc())


#  Inheritance : The ability to create Sub-classes that contain specializations of their parents


class ba1:
    def fun(self):
        print('sdsvcgvgvghvdgvds')


class sub(ba1):
    print('jchhfhv')


ob = sub()
ob.fun()

# Polymorphism : The ability to overload standard operators so that they have appropriate behavior based on their context


class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass


class cat(Animal):
    def talk(self):
        print('Meow')


class dog(Animal):
    def talk(self):
        print('woof')


# a = Animal()
# a.talk()

c = cat('kitty')
c.talk()

d = dog('Tommy')
d.talk()


# special methods


class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s,author:%s,pages:%s"% (self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book is destroyed')


book = Book("Inside Steve's Brain", "Leander Kahnew", 304)
print(book)
print(len(book))
del book


class Vector:
    def __init__(self, data):
        self.data=data

    def __str__(self):
        return repr(self.data)

    def __add__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] + other.data[j])
        return Vector(data)

    def __sub__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] - other.data[j])
        return Vector(data)


x = Vector([1, 2, 3])
y = Vector([4, 5, 6])
print(x+y)
print(x-y)


