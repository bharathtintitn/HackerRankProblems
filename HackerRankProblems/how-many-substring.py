'''
Consider a string of  characters, , of where each character is indexed from  to .

You are given  queries in the form of two integer indices:  and . For each query, count and print the number of different substrings of  in the inclusive range between  and .

Note: Two substrings are different if their sequence of characters differs by at least one. For example, given the string  aab, substrings  a and  a are the same but substrings  aa and  ab are different.

Input Format

The first line contains two space-separated integers describing the respective values of  and . 
The second line contains a single string denoting . 
Each of the  subsequent lines contains two space-separated integers describing the respective values of  and  for a query.

Constraints

String  consists of lowercase English alphabetic letters (i.e., a to z) only.
Subtasks

For  of the test cases, 
For  of the test cases, 
For  of the test cases, 
Output Format

For each query, print the number of different substrings in the inclusive range between index  and index on a new line.

Sample Input 0

5 5
aabaa
1 1
1 4
1 1
1 4
0 2
Sample Output 0

1
8
1
8
5
Explanation 0

Given  aabaa, we perform the following  queries:

    1 1: The only substring of a is itself, so we print  on a new line.
    1 4: The substrings of abaa are a, b, ab, ba, aa, aba, baa, and abaa, so we print  on a new line.
    1 1: The only substring of a is itself, so we print  on a new line.
    1 4: The substrings of abaa are a, b, ab, ba, aa, aba, baa, and abaa, so we print  on a new line.
    0 2: The substrings of aab are a, b, aa, ab, and aab, so we print  on a new line.
'''

from itertools import permutations as p

global_dict= dict()

def calc_substring(start, end, string, length, com):
    ''' Return nubmer of substring can be,
        formed from string, using start and end index.
    '''
    global global_dict
    try:
        a = global_dict[com]
        print a
        return
    except:
        pass

    if start == end:
        total = 1
    else:
        #store = set()
        store = dict()
        s = string[start:end+1]
        #print "going for string ", s
        length = end - start + 1
        count = 0
        total = 1
        for i in xrange(1,length):
            if i == 1:
                count = len(set(s))
            else:
                for j in xrange(0,length+1-i):
                    #store.add(s[j:j+i])
                    store[s[j:j+i]] = None
                    count += 1

                store = dict()
            total += count
            count = 0
    global_dict[com] = total
    print total

if __name__ == "__main__":
    row = map(int, raw_input().strip().split())
    n, q = row[0], row[1]
    string = raw_input().strip()
    #print "String got is ", string
    for _ in xrange(q):
        row = raw_input().strip()
        r = map(int, row.split())
        calc_substring(r[0], r[1], string, n, row)
