'''
Substring Diff

Given two strings of length , P = p1p2...pn and Q = q1q2...qn, we define  as the number of mismatches between  and . That is, in set notation,  refers to the size of the set
Given an integer , your task is to find the maximum length , such that there exists a pair of indices  for which we have . Of course, we should also have  and .

Input Format

The first line of input contains a single integer, , the number of test cases follow. 
Each test case consists of an integer, , and two strings,  and , separated by a single space.

Constraints

 length of 
  and  has the same length, their length not exceeding 1500.
  All characters in  and  are lower-case English letters.
  Output Format

  For each test case, output a single integer, , which is the maximum value for which there exists a pair of indices  such that .

  Sample Input

  3
  2 tabriz torino
  0 abacba abcaba
  3 helloworld yellomarin
  Sample Output

  4
  3
  8
  Explanation

  First test case: If we take "briz" from the first string, and "orin" from the second string, then the number of mismatches between these two substrings is equal to 2, and the length of these substrings are 4. Hence we have chosen i=3, j=2, L=4, and we have M(3,2,4) = 2.

  Second test case: Since S=0, we should find the longest common substring for the given input strings. We can choose "aba" as the result, and we don't have longer common substring between two strings. So, the answer is 3 for this test-case. That's we have chosen i=1, j=4, and L=3, and we have M(1,4,3)=0.

  Third test case: We can choose "hellowor" from first string and "yellomar" from the second string. So, we have chosen i=1, j=1, and L=8, and we have M(1,1,8)=3. Of course we can also choose i=2, j=2, and L=8 and we still have M(2,2,8)=3.
'''


def max_length(s, p, q):

    length_p = len(p)

    i = 0
    for incre in xrange(s, length_p, 1):
        for i in xrange(length_p - incre):
            str_p = p[i:incre]
            print 'p:',str_p
            for j in xrange(length_p - incre):
                str_q = q[j:incre]
                print "q:", str_q
                count = 0
                for k in xrange(len(str_q)):
                    print "q:%s and p:%s" % (str_q, str_p)
                    leng = len(str_q)
                    lengp = len(str_p)
                    if leng >= incre and lengp >= incre and str_q[j+k] != str_p[i+k]:
                        count += 1
                        if count == s:
                            print 'max len is', len(str_q)
                            return




if __name__ == "__main__":

    tests = int(raw_input().strip())
    for _ in xrange(tests):
        row = map(str, raw_input().strip().split())
        print row
        s = int(row[0])
        p = row[1]
        q = row[2]
        max_length(s, p, q)

