'''
Idea of this program is to find longest common subsequce from a given two strings.

Example:
    String A: abcedabc
    string B: bcedsaab
    output: bcedab

I am writing code to slove this problem using recursion.
Best method is to slove using Dynamic programming.
'''

def find_lcs(a, b, i, j, string):
    '''Print longest possible sub sequence'''
    if len(a) <= i or len(b) <= j:
        return string

    if a[i] == b[j]:
        string += a[i]
        i += 1
        j += 1
    else:
        j += 1

    one = find_lcs(a, b, i, j, string)
    two = find_lcs(a, b, i+1, j, string)
    if len(one) > len(two):
        return one
    return two

def lcs(a, b):
    '''Return longest possible sub sequence'''

    if len(a) > len(b):
        str_a = a
        str_b = b
    else:
        str_a = b
        str_b = a

    sub_str = ''
    for i in xrange(len(str_b)):
        print "Now iteration {}".format(i)
        sub = find_lcs(str_a, str_b, i, 0, '')
        if len(sub) > len(sub_str):
            sub_str = sub
    print sub_str
    return sub_str

if __name__ == "__main__":

    assert(lcs('abcedabc','bcedsaab'),'bcedab')
