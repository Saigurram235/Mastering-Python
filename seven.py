from pylab import *
from numpy import *
from KNN import *
import KNN
import mailbox
import numpy as np
import pandas as pd

# x = arange(50)*2*pi/50
# y = sin(x)
# print(x)
# print(plot(y))
# print(y)
# print(xlabel('index'))
# show()

# x = arange(50)*2*pi/50
# plot(x, sin(x), 'y-^')
# print(xlabel('index'))
# show()

#
#
# x = arange(50)*2*pi/50
# y = sin(x)
# print(scatter(x, y))
# show()


# x = rand(200)
# y = rand(200)
# size = rand(200)*50
# col = rand(200)
# print(scatter(x, y, size, col))
# print(colorbar())
# show()


# x = arange(50)*2*pi/50
# print(bar(x, sin(x), width= x[1] - x[0]))
# show()


# print(hist(randn(200)))
# show()


# def f(t):
#     s1 = cos(2*pi*t)
#     e1 = exp(-t)
#     return multiply(s1, e1)
#
#
# t1 = arange(0, 5, 0.1)
# t2 = arange(0, 5, 0.02)
# t3 = arange(0, 2, 0.01)
#
# subplot(211)
# i = plot(t1, f(t1), 'bo', t2, f(t2), 'k--')
# setp(i, 'markerfacecolor', 'r')
# grid(True)
# title('Sample of Three subplots')
# ylabel('y')
# xlabel('x')
#
# subplot(212)
# i = plot(t3, cos(2*pi*t3), 'g.')
# grid(True)
# ylabel('y')
# xlabel('x')
#
# show()


# def cd():
#     g = array([[1, 1.1], [1, 1], [0, 0.1]])
#     la = ['A', 'B', 'C']
#     return g, la
#
#
# g, la = cd()
# plot(g, la)
# show()


# def cd():
#     g = array([[1, 1.1], [1, 1], [0, 0.1]])
#     la = ['A', 'B', 'C', 'D']
#     return g, la
#
#
# g, la = KNN.createDataSet()
# print(KNN.classify0([1, 1], g, la, 3))

'''

s = pd.Series(list('98765'))
print(s)
print(s[2])

s = pd.Series(list('98765'), index=['A', 'B', 'C', 'D', 'E'])
print(s)
print(s['B'])
print(s[1])

s = pd.Series(range(5), index=list('vwxyz'))
print(s)
print(s['x'])

s = pd.Series(range(5), index=list('xwxyz'))
print(s)
print(s['x'])

s = pd.Series({1:10, 2:20, 3:30}, index=[1, 2, 3, 4, 5])
print(s)
print(s[4])

s = pd.Series({1:10, 2:20, 4:30}, index=[1, 2, 3, 4, 5])
print(s)
print(s[4])
print(s*4)

data = {'Country': ['Us', 'Us', 'Ind', 'Ind'],
        'Years': [2012, 2013, 2012, 2013]}
df = pd.DataFrame(data)
print(df)

data = {'Us': {2012:30, 2013:35},
        'Ind': {2012:20, 2013:25, 2014:14, 2015:85}}
df = pd.DataFrame(data)
print(df)
print(df['Ind'])
print(df.describe())


data = {'Country': ['Us', 'Us', 'Ind', 'Ind'],
        'Years': [2012, 2013, 2012, 2013], 'Population': [30, 60, 90, 120]}


df = pd.DataFrame(data)
df['CorrectPopulation'] = df['Population']*1.5
print(df)

'''

# ob = pd.Series(['hadoop', 'CSS', 'R'], index=[1, 3, 5])
# print(ob)
# print(ob.reindex(range(4)))
# print(ob.reindex(range(6), fill_value='Python'))


# fname = 'C:/Users/gurra/OneDrive/Desktop/Coursera/Introduction to Data Science in Python/census.csv'
# data = pd.read_csv(fname)
# print(data.head())
# print(data.columns)
# print(len(data))
# print(data['SUMLEV'])
# print(data.SUMLEV)
# data.SUMLEV.hist()
# show()
# print(data.irow(1))
# print(data[data.SUMLEV == 40])
# gg = data[data.SUMLEV == 40]
# print(gg.head())




