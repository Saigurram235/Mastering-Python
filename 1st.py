from textblob import TextBlob

print("Hello")
x = [0, 1, 2, 3]
print(x)

a = 5
b = 5

print(not a==b)

print('aaaa' + 'ASDXC')

print('sddd'*452)

v = 'dsd'
print(type(v))


p = ' I am good $$$$$'
x = p.strip()
print(p.strip())
print(p.replace(' ', ''))
print(p.replace('$', '+'))
print(p.replace('$', '+').strip())

c = 'Sai Gurram'
print(c[2], c[6])
print(c.split())
print(len(c))
for m in c:
    print(m)

print(c.replace('a', 'A'))
print(c.replace('a', 'A', 1))
print('saigurram'.replace('a', 'A'))

print('a' in c)
print('x' in c)
print('Sai' in c)

print('My name is %s, I am %s, My Roll number is %d' %('Sai','Student', 123456))

c = 'edureka'
print(c.capitalize())
print(c.lower())
print(c.upper())

'''
s = unicode(c)
print(s)
print(s.encode())
print(unicode(c, "utf-8"))

hindiString = u"बिपाशा और करण सिंह को दो टीवी शो होस्ट करने का ऑफर"
strhindiString = "बिपाशा और करण सिंह को दो टीवी शो होस्ट करने का ऑफर"

print(type(hindiString))
print(type(strhindiString))

print(hindiString.encode(encoding='UTF-8',errors='strict'))
print(strhindiString.decode(encoding='UTF-8',errors='strict'))

'''

s = 'edureka'
print(s.count('e',0,len(s)))
print(s.count('e'))

# a = s.encode('base64', 'strict')
# print(a)
#
# b = a.decode('base64', 'strict')
# print(b)

# print(s.index('re', 0, len(b)))
# print(s.index('re'))

#
# hindiString = u"बिपाशा और करण सिंह को दो टीवी शो होस्ट करने का ऑफर"
# hblob = TextBlob(hindiString)
# print(hblob.detect_language())
# print(hblob.translate(to='en'))

# 20322959
# Gurramkalyan123





