import sys

print('Number of Arguments :', len(sys.argv),'arguments')
print('Argument List', str(sys.argv))

# name = raw_input("Input as a string: ")
# print(type(name))


number = input("Formatted input ")
print(type(number))

value = 10

if value < 10:
    print('Answer is less than 10')
else:
    print('Answer is greater than 10')

num = 0
while num < 3:
    print('The count is:', num)
    num += 1

for letter in '124356':
    print('Int Value: ', int(letter))

# in operator for if and for behaves differently


num_array = [ 1, 2, 3, 4, 5]

for num in num_array:
    if num == 0:
        print('Object Found')
else:
    print('No Object Found')

print(range(5))

print(range(5, 10))

print(range(5, 10, 2))


mylist = list()

mylist = range(5)
mylist = list(range(5))

name = 'edureka'
mylist = list(name)

# List Maintain the Original Order
mylist =  [ "Python", "Hadoop", "DataScience", "Stats"]
mylist[-1]
mylist[-2]
mylist[1:3]
mylist[2:]
mylist[:2]
mylist[1:-1]

mylist[2] = "Programming"
mylist.append("DataEngineering")
mylist.pop()

mylist.remove("Programming")
newlist = ["Programming", "SystemAnalysis"]
mylist.extend(newlist)

mylist.index("Hadoop")
"Programming" in mylist

mylist = mylist + ["Mathematics", "DomainKnowledge"]

list1 = ['Programming', 'DomainKnowledge']
list2 = ['Python', 'SystemAnalysis', 'Hadoop']
list3 = ['Stats',  'Mathematics']
mylist = [list1, list2, list3]
mylist[0]
mylist[0][1]


mylist.extend([1,2,3,4])

mylist = [ "Jack", 105, 120.5, ["Python", "Perl"] ]
mylist += [ "Joe", 106, 200.5, ["JavaScript", "Django"]]


lang = ( "Python", "Java", "R", "C", "Scala")
lang[-1]
lang.index('Python')
# lang.append("Haskel") For tuple append function doesn't work


for lang_name in lang:
    print(lang_name)

langlist = list(lang)


t1 = (1, 2)
t2 = (1, 3)

# cmp(t1, t2)

tuple(enumerate(langlist))


# xrange(4)
#
# for x in xrange(4):
#     print (x)

Info = {}

Info = {1: 'Python', 2: 'Hadoop'}
print(Info)

print(Info[1])
print(Info[2])

print(len(Info))

SalaryAnalysis = {'Python': 50, 'Hadoop': 70, 'R': 45, 'Java': 25 , 'Scala': 200, 'Pascal':5}

print(SalaryAnalysis['Python'])

print('Scala' in SalaryAnalysis)

print(SalaryAnalysis.keys())
print(SalaryAnalysis.values())
print(SalaryAnalysis.items())

print(SalaryAnalysis.get('Python'))

ExternalAnalysis = { 'Haskel': 5, 'Lisp': 10 }
print(SalaryAnalysis.update(ExternalAnalysis))

print(SalaryAnalysis.pop('Python'))

for key,value in SalaryAnalysis.items():
    print(key,value)

for key in SalaryAnalysis.keys():
    print(key, SalaryAnalysis[key])

for key in SalaryAnalysis:
    print(key,SalaryAnalysis[key])


# In order access
SalaryAnalysis = {'Python': 50, 'Hadoop': 70, 'R': 45, 'Java': 25 , 'Lisp': 10, 'Haskel':5}

keyinorder = sorted(SalaryAnalysis.keys())
for key in keyinorder:
    print(key, '=>', SalaryAnalysis[key])

for key in SalaryAnalysis:
    print(key, '=>', SalaryAnalysis[key])


SalaryAnalysis.items()
import operator
sortedSalaryAnalysis = sorted(SalaryAnalysis.items(), key=operator.itemgetter(1))
sortedSalaryAnalysis = sorted(SalaryAnalysis.items(), key=operator.itemgetter(1), reverse = True)


langlist1 = ('Python', 'C', 'C++', 'Java', 'Haskel', 'Lisp', 'Scala', 'Python')
langlist2 = ('SmallTalk', 'Perl', 'Java', 'Python', 'Pascal', 'Perl' )

print(set(langlist1))
print(set(langlist2))

setlanglist1 = set(langlist1)
setlanglist2 = set(langlist2)

print(setlanglist1|setlanglist2)
print(setlanglist1&setlanglist2)
print(setlanglist1-setlanglist2)

f = open("x.txt")
f
f.__enter__()
f.readline()
f.__exit__(None, None, None)


with open("x.txt") as f:
    print (f.readline())


#Converting  zip to tar

import tarfile
import zipfile

import StringIO, sys, time
now = time.time()

zip = zipfile.ZipFile('x.zip', 'r')
tar = tarfile.open('x.tar.gz', "w:gz")
tar.posix = 1

data = zip.read('x.txt')
data = data.replace("\r\n", "\n")

tarinfo = tarfile.TarInfo()
tarinfo.name = 'x.txt'
tarinfo.size = len(data)
tarinfo.mtime = now
tarinfo.uname = tarinfo.gname = "ubuntu"
tarinfo.uid = tarinfo.gid = 1000
tar.addfile(tarinfo, StringIO.StringIO(data))


tar.close()
zip.close()


import sys, os
for root, dirs, files in os.walk('/home/ubuntu/pythonclass', topdown=True):
    for name in files:
        fileName = str(os.path.join(root, name))
        print(fileName)
        if 'zip' in fileName:
            print('Zip File name', fileName)



