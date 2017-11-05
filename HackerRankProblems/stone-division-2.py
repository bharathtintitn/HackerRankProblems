'''
You have a pile of  stones that you want to split into multiple piles, as well as a set, , of  distinct integers. We define a move as follows:

    First, choose a pile of stones. Let's say that the chosen pile contains  stones.
    Next, look for some  such that  and  is divisible by  (i.e.,  is a factor of ); if such an  exists, you can split the pile into  equal smaller piles.
    You are given  queries where each query consists of  and . For each query, calculate the maximum possible number of moves you can perform and print it on a new line.

    Input Format

    The first line contains an integer, , denoting the number of queries. The  subsequent lines describe each query in the following format:

        The first line contains two space-separated integers describing the respective values of  (the size of the initial pile in the query) and  (the size of the set in the query).
        The second line contains  distinct space-separated integers describing the values in set .
        Constraints

        Subtask

         for  of the maximum score.
         Output Format

         For each query, calculate the maximum possible number of moves you can perform and print it on a new line.

         Sample Input 0

         1
         12 3
         2 3 4
         Sample Output 0

         4
'''
def find_max(array, total, i, div,result):

    if i < 0:
        return total
    new_div, new_quo = divmod(result, array[i])
    if new_quo == 0 and array[i] <> total:
       total = (div* 1) + total
       result = array[i]
       div = new_div

    i -= 1
    return find_max(array, total, i, div, result)



if __name__ == "__main__":

    task = int(raw_input().strip())
    for _ in xrange(task):
        row = map(int, raw_input().strip().split())
        result = row[0]
        length = row[1]
        row = map(int, raw_input().strip().split())
        array = sorted(row)
        #import pdb
        #pdb.set_trace()
        print find_max(array, 0, length-1, 1, result)
