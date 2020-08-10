

def palindrome(string, index, sub_len, length):

    if index + sub_len <= length:
        palindrome(string, index + 1, sub_len, length)
    else:
        return
    a = string[index:index+sub_len]
    if a == a[::-1]:
        print a

if __name__ == "__main__":

    string = 'bhara'
    length = len(string)
    if length % 2 == 0:
        mid = length/2 + 1
    else:
        mid = (length/2) + 1
    print "Mid: ", mid
    for i in xrange(mid):
        palindrome(string, 0, i, length)
