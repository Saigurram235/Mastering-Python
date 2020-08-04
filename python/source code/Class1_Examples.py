import string

from numpy.core import unicode

string.ascii_letters

string.digits

import random
pwd = ".".join(random.choice(string.ascii_letters + string.digits) for _ in range(25))


# pip freeze







#Encoding / Decoding 

s = "hello byte string"
u = unicode( s )
backToBytes = u.encode()

s = "hello normal string"
u = unicode( s, "utf-8" )
backToBytes = u.encode( "utf-8" )

isinstance( s, str )
isinstance( u, unicode )


hindiString = u"बिपाशा और करण सिंह को दो टीवी शो होस्ट करने का ऑफर"
strhindiString = "बिपाशा और करण सिंह को दो टीवी शो होस्ट करने का ऑफर"

type(hindiString)
type(strhindiString)

hindiString.encode(encoding='UTF-8',errors='strict')
strhindiString.decode(encoding='UTF-8',errors='strict')


#Strings are decoded to Unicode and Unicodes are encoded to strings

s = 'cafe'
len(s)

u = u"café"
len(u)

s = "café"
len(s)
s.decode("utf-8") # Converted in Decode

len(s.decode("utf-8"))
u.encode( "utf-8" )




from textblob import TextBlob
hindiString = u"बिपाशा और करण सिंह को दो टीवी शो होस्ट करने का ऑफर"
hblob = TextBlob(hindiString)
hblob.detect_language()
hblob.translate(to='en')



