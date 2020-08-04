import subprocess
from functools import reduce

from numpy.random.mtrand import choice


def outfunc(a, b, c):
    print(a, b, c)

    def innerfunc(x, y):
        print(x, y)

    innerfunc(a, b)


outfunc(1, 2, 3)


def add(mylist):
    mylist.append('Python')


mylist = ['Edureka']

add(mylist)

print(mylist)


def add(mylist):
    mylist = []


mylist = ['Edureka']

add(mylist)

print(mylist)


def fun(a, b, c):
    print(a, b, c)


def fun(aval=3, bval=[], cval=()):
    print(aval)

    for b in bval:
        print(b)

    for c in cval:
        print(c)


fun()
fun(4)
fun(5, ['A', 'B'])
fun(6, ['A', 'B'], ('a', 'b'))


def fun(a, b, c):
    print(a, b, c)


fun(c=3, b=2, a=1)


def funNew(**arr):
    for k in arr.keys():
        print(k, ":", arr[k])


funNew(a='Edureka', b='Python')
funNew(a='Edureka', b='Python', c='Hadoop')

# funNew({'a': 'Edureka', 'b': 'Python'})  # check


def funr(*arr):
    for val in arr:
        print(val)


funr(1, 2, 3, 4)
funr(1, 2, 3)
funr()
funr(1, 2, 3, 4, 5)


def fun():
    try:
        data = 10 / 0
    except:
        pass
    else:
        print(' I am else ')
    print('ignored exception')


fun()

tup = (20, 10, 30, 100, 90, 70)
print(sorted(tup))
print(sorted(tup, reverse=True))

mylist = [20, 10, 30, 100, 90, 70]
mylist.sort()

# Lambda Function

incr = lambda num, sum=5: num + sum

incr(5)
incr(5, 10)
# incr(5, 10, 15)  # Check


def incrfun():
    return lambda num, sum=5: num + sum


f = incrfun()
f(5)
f(5, 10)


# lambda Basics
# lambda argument1, argument2,... argumentN :expression using arguments

def func(x, y, z): return x + y + z


func(1, 2, 3)

f = lambda x, y, z: x + y + z
f(1, 2, 3)

L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[0](3))


def lower(x, y):
    if x < y:
        return x
    else:
        return y


lower('bb', 'aa')
lower('aa', 'bb')

lower = (lambda x, y: x if x < y else y)
lower('bb', 'aa')
lower('aa', 'bb')


#
def action(x):
    return (lambda y: x + y)


act = action(99)
act
act(100)

# map
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)
updated


def inc(x): return x + 10


updated = list(map(inc, counters))

updated = list(map((lambda x: x + 3), counters))

# filter

list(range(-5, 5))
res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)

list(filter((lambda x: x > 0), range(-5, 5)))
list(filter((lambda x: x > 0), [0, 1, 2, 3, 4, 5]))

L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res = res + x

reduce((lambda x, y: x + y), [1, 2, 3, 4])
reduce((lambda x, y: x * y), [1, 2, 3, 4])

from operator import itemgetter

itemgetter(2)(range(1, 10))

Edureka_Courses = [('Hadoop', 2), ('Nosql', 1), ('ETL', 3), ('Hadoop', 4)]
sorted(Edureka_Courses, key=itemgetter(1))
sorted(Edureka_Courses, key=itemgetter(0))
# sorted by index 0 then index 1
sorted(Edureka_Courses, key=itemgetter(0, 1))
sorted(Edureka_Courses, key=itemgetter(1, 0))

dir(list)

import sys, os

if os.path.exists('/home/ubuntu/pythonclass'):
    print('Path exists')

for root, dirs, files in os.walk('/home/ubuntu/pythonclass', topdown=True):
    for name in files:
        fileName = str(os.path.join(root, name))

        print(fileName)
        if 'zip' in fileName:
            print('Zip File name', fileName)

check = subprocess.call(['hadoop', 'fs', '-lsr', '/'])

import datetime

datetime.datetime.now()
str(datetime.datetime.now())

import time;

epoch = time.time()
datetime.datetime.fromtimestamp(epoch)

dt = datetime.datetime.now()
dt.timetuple()
time.mktime(dt.timetuple())

dt1 = datetime.datetime(2016, 7, 29, 4, 0, 0)
dt - dt1
(dt - dt1).days
(dt - dt1).seconds
(dt - dt1).miliseconds
(dt - dt1).total_seconds()

# formating
dt.strftime("%d/%m/%y")
dt.strftime("%d/%m/%Y")
dt.strftime("%A %d. %B %Y")

dt.day
dt.hour
dt.year
dt.month

dtnew = datetime.strptime("30/07/2016 16:30", "%d/%m/%y %H:%M")
dtnew = datetime.datetime.strptime("30/07/2016 16:30", "%d/%m/%Y %H:%M")

# refer to https://docs.python.org/2/library/datetime.html

dt - datetime.timedelta(days=5)

import numpy as np

cvalues = [25.3, 24.8, 26.9, 23.9]
C = np.array(cvalues)
print(C)
print(type(C))

print(C * 9 / 5 + 32)

fvalues = [x * 9 / 5 + 32 for x in cvalues]

fvalues = []
for x in cvalues:
    fvalues.append(x * 9 / 5 + 32)

a = np.arange(1, 10)
print(a)

print(range(1, 10))

x = np.arange(0.5, 10.4, 0.8)
print(x)

# 50 values between 1 and 10:
print(np.linspace(1, 10))
# 7 values between 1 and 10
print(np.linspace(1, 10, 7))
samples, spacing = np.linspace(1, 10, retstep=True)

# numpy.ndarray
X = np.linspace(1, 10, 20)
Y = np.linspace(10, 20, 20)
Z = X + Y
print(Z)

x = np.array(42)
print("The dimension of x:", np.ndim(x))

V = np.array([3.4, 6.9, 99.8, 12.8])
print("Dimension of V: ", np.ndim(V))

A = np.array([[3.4, 8.7, 9.9],
              [1.1, -7.8, -0.7],
              [4.1, 12.3, 4.8]])
print(A)
print(A.ndim)

# Shape of an Array
x = np.array([[67, 63, 87],
              [77, 69, 59],
              [85, 87, 99],
              [79, 72, 71],
              [63, 89, 93],
              [68, 92, 78]])
print(np.shape(x))

x.shape = (3, 6)
print(x)

x.shape = (2, 9)
print(x)

# x.shape = (4, 4)

A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]])
print(A[0, 0])
for i in range(0, A.ndim):
    print(A[i, i])

print(A[:3, 2:])
print(A[:, 4:])

X = np.arange(28).reshape(4, 7)
print(X)
# X[start:stop:step]

print(X[::2, ::3])

# Note slicing in list & tuple create new list & tuple but
# In ndarray it gives a view

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
S = A[2:6]
S[0] = 22
S[1] = 23
print(A)

# Arrays of Ones and of Zeros
E = np.ones((2, 3))
print(E)
F = np.ones((3, 4), dtype=int)
print(F)

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
S = A.copy()
S[0] = 22
S[1] = 23
print(A)
print(S)

# Exercise
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 200
print(a[1])

# (3.21, 1.77, 3.65) = 3.21 � (1,0,0) + 1.77 (0,1,0) + 3.65 � (0,0,1)
x = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
y = ([3.65, 1.55, 3.42])
scalars = np.linalg.solve(x, y)
print(scalars)

# Probability
import random

outcome = random.randint(1, 6)
print(outcome)

[random.randint(1, 6) for _ in range(10)]

outcome = np.random.randint(1, 7, size=10)
print(outcome)

print(np.random.randint(1, 7, size=(5, 4)))

mylist = ["Python", "Hadoop", "DataScience", "Stats"]
print(choice(mylist))

x = np.random.random_sample((3, 4))  # between 0.0 to 1
print(x)

x = np.matrix(((2, 3), (3, 5)))
y = np.matrix(((1, 2), (5, -1)))

x * y

# dot product
np.dot(x, y)

userdata = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                          'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                          'The Night Listener': 3.0},
            'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                             'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                             'You, Me and Dupree': 3.5},
            'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                 'Superman Returns': 3.5, 'The Night Listener': 4.0},
            'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                             'The Night Listener': 4.5, 'Superman Returns': 4.0,
                             'You, Me and Dupree': 2.5},
            'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                             'You, Me and Dupree': 2.0},
            'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                              'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
            'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}

userdata['Lisa Rose']['Lady in the Water']

# similarity score
# similarity scores:
# Euclidean distance
# and Pearson correlation
# (x1,y1) and (x2,y2)
# euclidean distance

from math import sqrt

sqrt(pow(5 - 4, 2) + pow(4 - 1, 2))

1 / (1 + sqrt(pow(5 - 4, 2) + pow(4 - 1, 2)))
userdata['Lisa Rose']
userdata['Gene Seymour']

common_movies = set(userdata['Lisa Rose'].keys()) & set(userdata['Gene Seymour'].keys())
sum_score = 0.0
for movie in common_movies:
    sum_score += pow(userdata['Lisa Rose'][movie] - userdata['Gene Seymour'][movie], 2)

similarity_score = 1 / sum_score


def sim_distance(udata, person1, person2):
    sum_score = 0
    common_movies = set(udata[person1].keys()) & set(udata[person2].keys())
    for movie in common_movies:
        sum_score += pow(userdata[person1][movie] - userdata[person2][movie], 2)
        similarity_score = 1 / sum_score
    return similarity_score


sim_distance(userdata, 'Lisa Rose', 'Gene Seymour')


def topMatches(udata, person, n, similarity):
    scores = [(similarity(udata, person, other), other) for other in udata if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]


person = 'Toby'
for other in userdata:
    if not other == person:
        sscore = sim_distance(userdata, person, other)
        print(person, '==', other, sscore)

sscore_list = [(sim_distance(userdata, person, other), other) for other in userdata if not other == person]

addscore = 0.0
for sscore, other in sscore_list:
    addscore += sscore

addscore = sum([sscore for sscore, other in sscore_list])
normalized_sscore_list = [(sscore / addscore, other) for sscore, other in sscore_list]

sorted(normalized_sscore_list, key=lambda x: x[0])
sorted(normalized_sscore_list, key=lambda x: x[0], reverse=True)

userdata['Toby']
userdata['Mick LaSalle']

normalized_sscore_hash = {}
for score, name in normalized_sscore_list:
    normalized_sscore_hash.setdefault(name, score)

rank = {}
for other in userdata:
    if other == person: continue
    for movie in userdata[other]:
        if movie not in userdata[person]:
            rank.setdefault(movie, 0)
            rank[movie] += userdata[other][movie] * normalized_sscore_hash[other]
