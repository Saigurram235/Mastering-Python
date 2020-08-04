import sqlite3

# Debugging i Python

# Unit Testing

# def is_equal(a, b):
#     if a == b:
#         return True
#     return False

# Database sqlite3

# sqlite3.version


# db = sqlite3.connect(':memory:')
# db = sqlite3.connect('edureka')
#
#
# cursor = db.cursor()
# cursor.execute('''CREATE TABLE custs(id INTEGER PRIMARY KEY, name TEXT, phone  TEXT, email TEXT unique, password
# TEXT)''')
# cursor.execute('''CREATE TABLE custs1(id INTEGER PRIMARY KEY, name TEXT, phone  TEXT, email TEXT unique, password
# TEXT)''')
# cursor.execute('''CREATE TABLE custs2(id INTEGER PRIMARY KEY, name TEXT, course TEXT)''')

# if cursor.execute('''INSERT INTO custs2(name, course) VALUES(?,?)''',('Sai', 'Python')):
#     print('Record Inserted Successfully')

# if cursor.execute('''INSERT INTO custs2(name, course) VALUES(?,?)''',('Sai2', 'java-Python')):
#     print('Record Inserted Successfully')

#
# if cursor.execute('''INSERT INTO custs2(name, course) VALUES(:name,:course)''', {'name':'Sai', 'course': 'Python'}):
#     print('Record Inserted Successfully')

# if cursor.executemany('''INSERT INTO custs2(name, course) VALUES(?,?)''', [('Sai2','Python'), ('Smith', 'Hadoop')]):
#     print('Record Inserted  Multiple Values Successfully')

# db.commit()
#
# if cursor.execute('''SELECT name, course FROM custs2'''):
#     print('Records fetched successfully')
# r1 = cursor.fetchone()
# print(r1)

# recordAll = cursor.fetchall()
# print(recordAll)

# for r in recordAll:
#     print('{0}, {1}'.format(r[0],r[1]))

# if cursor.execute('''INSERT INTO custs2(name, course) VALUES(?,?)''', ('Sai5','P')):
#     print('Record Inserted Successfully')
# cursor.lastrowid

# if cursor.execute('''SELECT name, course FROM custs2 WHERE name=?''', ('Sai',)):
#     print('Records fetched successfully')
#
# for r in cursor:
#     print(r)

# if cursor.execute('''Update custs2 SET course = ? WHERE name = ?''', ('Java','Sai')):
#     print('Record updated Successfully')
#
# if cursor.execute('''SELECT name, course FROM custs2 WHERE name=?''',('Sai',)):
#     print('Records fetched successfully')
# print(cursor.fetchone())

# db.rollback()


# if cursor.execute('''SELECT name, course FROM custs2 WHERE name=?''', ('Sai',)):
#     print('Records fetched successfully')
#
# Recordsfetchedsuccessfully
# print(cursor.fetchone())
# ('Sai', 'Python')


# if cursor.execute('''DELETE FROM custs2 WHERE name=?''', ('Sai',)):
#     print('Records Deleted successfully')
#
# db.commit()

# if cursor.execute('''SELECT COUNT(*) FROM custs2 WHERE name=?''', ('Sai',)):
#    print('Records fetched successfully')
# print(cursor.fetchone())

# if cursor.execute('''SELECT COUNT(*) FROM custs2 WHERE name=?''', ('Smith',)):
#     print('Records fetched successfully')
#
# print(cursor.fetchone())


# File Handling To Read Write

# f = open('file path')
# line = f.readline()

# In this pass all lines at a time
# for l in f.readline():
#     print(l)

# In this pass one line at a time
# for l in f:
#   print(l)

# output = open('file path', 'w')
# f = open('file path')
# If we read 10 it will read 1 bytes
# f.read(1)

# If we read 10 it will read 10 bytes
# f.read(10)

# If we read 10 it will read all
# f.read()

# output = open('D:/python-online class/out.txt', 'w')
# # output.write('hello text file\n')
# # output.close()
# #
# # f = open('D:/python-online/classout.txt')
# # line = f.readline()
# # print(line)

