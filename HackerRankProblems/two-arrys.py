'''
Consider two -element arrays of integers,  and . You want to permute them into some  and  such that the relation  holds for all  where . For example, if , , and , a valid  satisfying our relation would be  and .

You are given  queries consisting of , , and . For each query, print YES on a new line if some permutations ,  exist satisfying the relation above. If no valid permutations exist, print NO instead.

Input Format

The first line contains an integer, , denoting the number of queries. The  subsequent lines describe each of the  queries in the following format:

    The first line contains two space-separated integers describing the respective values of  (the size of arrays and ) and  (the relation variable).
    The second line contains  space-separated integers describing the respective elements of array .
    The third line contains  space-separated integers describing the respective elements of array .
    Constraints

    Output Format

    For each query, print YES on a new line if valid permutations exist; otherwise, print NO.

    Sample Input

    2
    3 10
    2 1 3
    7 8 9
    4 5
    1 2 2 1
    3 3 3 4
    Sample Output

    YES
    NO
    Explanation

    We perform the following two queries:

        , , and . We permute these into  and  so that the following statements are true:

            Thus, we print YES on a new line.

            , , and . To permute  and  into a valid  and , we would need at least three numbers in  to be greater than ; as this is not the case, we print NO on a new line.
'''
def two_array(a, b, n, k):

    a = sorted(a)
    b = sorted(b, reverse=True)
    print a
    print b
    for i, j in zip(a,b):
        if i+j < k:
            print "NO"
            return
    print "YES"



if __name__ == "__main__":

    queries = int(raw_input().strip())
    for _ in xrange(queries):
        row = map(int, raw_input().strip().split())
        n, k = row[0], row[1]
        a = map(int, raw_input().strip().split())
        b = map(int, raw_input().strip().split())
        two_array(a, b, n, k)

