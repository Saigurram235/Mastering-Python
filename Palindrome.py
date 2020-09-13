import Dequeue


def Palindrome(item):
    d = Dequeue.Dequeue()
    for i in item:
        d.add_rear(i)

    flag = True

    while d.size() > 1 and flag:
        first_string = d.remove_front()
        last_string = d.remove_rear()
        if first_string != last_string:
            flag = False

    if flag:
        return 'It is a Palindrome'
    else:
        return 'it is not a Palindrome'

print(Palindrome('radar'))
print(Palindrome('dcbhbchehcd'))