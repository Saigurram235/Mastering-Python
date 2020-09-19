import re

# def Palindrome_Recursion(string):
#     n = len(string)
#     print(n)
#     if n > 1:
#         if string[0] == ' ' or string[n-1] == ' ':
#             if string[0] == ' ':
#                 Palindrome_Recursion(string[1:])
#             elif string[n-1] == ' ':
#                 Palindrome_Recursion(string[:n-2])
#             else:
#                 Palindrome_Recursion(string[1:n-2])
#         elif string[0] in "~`!@#$%^&*()_;:'.," or string[n-1] in "~`!@#$%^&*()_;:'.,":
#             if string[0] in "~`!@#$%^&*()_;:'.,":
#                 Palindrome_Recursion(string[1:])
#             elif string[n-1] in "~`!@#$%^&*()_;:'.,":
#                 Palindrome_Recursion(string[:n-2])
#             else:
#                 Palindrome_Recursion(string[1:n-2])
#         else:
#             # flag = True
#             if string[0] == string[n-1]:
#                 Palindrome_Recursion(string[1:n-2])
#             else:
#                 return 'it is not'
#             # if flag:
#             #     return 'It is Palindrome'
#             # else:
#             #     return 'It is not Palindrome'
#     else:
#         return 'it is'
#
# print(Palindrome_Recursion("radar"))
# print(Palindrome_Recursion("madam i'm adam"))

'''
# Python program to find if a sentence is
# palindrome
# To check sentence is palindrome or not
def sentencePalindrome(s):
    l, h = 0, len(s) - 1

    # Lowercase string
    s = s.lower()

    # Compares character until they are equal
    while (l <= h):

        # If there is another symbol in left
        # of sentence
        if (not (s[l] >= 'a' and s[l] <= 'z')):
            l += 1

        # If there is another symbol in right
        # of sentence
        elif (not (s[h] >= 'a' and s[h] <= 'z')):
            h -= 1

        # If characters are equal
        elif (s[l] == s[h]):
            l += 1
            h -= 1

        # If characters are not equal then
        # sentence is not palindrome
        else:
            return False
    # Returns true if sentence is palindrome
    return True


# Driver program to test sentencePalindrome()
s = "Too hot to hoot."
if (sentencePalindrome(s)):
    print "Sentence is palindrome."
else:
    print "Sentence is not palindrome."
'''

# This code is contributed by Sachin Bisht


# def sentencePalindrome(s):
#     if 1 < len(s):
#         if not('a' <= s[0] <= 'z'):
#             print(s[0])
#             sentencePalindrome(s[1:])
#             print(s[1:])
#         elif not('a' <= s[len(s) - 1] <= 'z'):
#             sentencePalindrome(s[:len(s)-1])
#         elif s[0] == s[len(s)-1]:
#             sentencePalindrome(s[1:len(s)-1])
#         else:
#             return 'It is not palindrome'
#     else:
#         return 'It is Palindrome'
#
#
# print(sentencePalindrome("madam i'm adam"))


def sentencePalindrome(sentence):
    sentence = re.sub('[^\w]', '', sentence.lower())
    if len(sentence) == 1:
        return True
    elif len(sentence) == 2:
        return sentence[0] == sentence[1]
    else:
        return sentencePalindrome(sentence[1:-1])


x = sentencePalindrome("madam i'm adam")
if x:
    print('It is palindrome')
else:
    print('It is not Palindrome')







