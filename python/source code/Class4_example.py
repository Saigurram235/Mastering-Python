import re
import string

re.search('ab', 'Here is an absolute string')

r = re.search('ab', 'Here is an absolute string')
r.group()
r.group(1)
r.start()
r.end()

# start,end
r.span()


m = re.match(r"(..)+", "edureka")

emailstring = 'john@gmail.com, harry@yahoo.com, dean@gmail.com'

gmails = re.findall(r'[\w\.-]+@gmail[\w\.-]+',emailstring)

for email in gmails:
    print(email)

emailstring = 'john@gmail.com, harry@yahoo.com, dean@gmail.com'
re.sub('gmail', 'yahoo', string)

# Literals
'''
The quick brown fox jumps over the lazy dog
/fox/

To be, or not to be
/be/

this is outside (this is inside)
/(this is inside)/   could not match ( or ) as they are meta chars

this is outside (this is inside)
/\(this is inside\)/


12 meta chars

• Backslash \
• Caret ^
• Dollar sign $
• Dot .
• Pipe symbol |
• Question mark ?
• Asterisk *
• Plus sign +
• Opening parenthesis (
• Closing parenthesis )
• Opening square bracket [
• The opening curly brace {

#Character classes with square brackets

licence and license are valid
/ licen[cs]e /

[0-9] = digit
[a-z] =  lowercase letter
[A-Z] =  upper letter

if we want to match any lowercase or uppercase alphanumeric
character then we use [0-9a-zA-Z]

Another possibility—the negation
[^0-9] match anything but non-digit char

/hello[^0-9]/

Some predefined Char Class

. match anything except \n
\d match [0-9]
\D [^0-9]
\s [\t\n\r\f\v]
\S [^\t\n\r\f\v]
\w [a-zA-Z0-9_]
\W [^a-zA-Z0-9_]

# Alteration

/yes|no/ matches both string "yes" and "no"

Driving Licence: yes
/Licence: yes|no/

Quantifiers : for repeat characters
meta char used
? match 0 or 1 time
* match 0 or more times
+ match 1 or more times
{n,m} between n to m times

/cars?/
car is matched one
s can be matched 0 or 1 time

so essentially : "car" or "cars" both will match.

Suppose you have ph numbers such as  
555-555-555 
555 555 555
555555555

all these can be matched by 
/\d+[-\s]?\d+[-\s]?\d+/

/\ d{1,3}[- \ s]?\ d{3}[- \ s]?\ d{3}/

 "Hello", Master "Python"
 /".+"/ will match everything ? Because it used greedy approach
 
Boundary Matching
^ beginning
$ end of a line
\b word boundary

/^Name:/ would mean match from beginning

/^Name:[\sa-zA-Z]+$/
will match 
Name:    Somil
Name:  JOHN

/\bhello\b/ will only match string with hello such 

"hello master python"
 but /hello/ will also match
 
 "othello is a nice game"
 "helloed out"


'''

import re

pattern = re.compile(r'\bfoo\b')

pattern.match("foo bar")

pattern.match("bar")

pattern = re.compile("\\\\")

pattern.match("\\author")

pattern.match("author")

pattern = re.compile(r'<HTML>')
pattern.match("<HTML><head>")

pattern.match("    <HTML>")
pattern.search("    <HTML>")
pattern.search("    \n<HTML>")


pattern = re.compile(r"\w+")
pattern.findall("hello world")

pattern = re.compile(r'a*')

pattern.findall("aba")

pattern = re.compile(r"(\w+) (\w+)")

match = pattern.search("Hello world")

match.group() # returns the entire match string

match.group(0)

match.group(1)

match.group(2)


pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")

match = pattern.search("Hello world")

match.group('first')

match.group('second')


pattern = re.compile("^\w+\: (\w+/\w+/\w+)")

pattern.findall("date: 12/01/2013 \ndate: 11/01/2013")

pattern = re.compile("^\w+\: (\w+/\w+/\w+)", re.M)

pattern.findall("date: 12/01/2013 \ndate: 11/01/2013")

re.findall(r"\w+", "اذه⇢لاثم")

re.findall(r"\w+", "这是一个例子")


