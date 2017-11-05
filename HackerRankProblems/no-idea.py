'''
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints 
 
  

  Input Format

  The first line contains integers  and  separated by a space. 
  The second line contains  integers, the elements of the array. 
  The third and fourth lines contain  integers,  and , respectively.

  Output Format

  Output a single integer, your total happiness.

  Sample Input
  3 2
  1 5 3
  3 1
  5 7

  Sample Output
  1

  Explanation

  You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set does not exist in the array so it is not included in the calculation.

  Hence, the total happiness is 2-1=1.

'''



def no_idea(setA, setB, array, n, m):
    happiness = 0
    for i in array:
        if i in setA:
            happiness += 1
        if i in setB:
            happiness -= 1

    print happiness

if __name__ == "__main__":

    row  = map(int, raw_input().strip().split())
    n, m = row[0], row[1]

    array = map(int, raw_input().strip().split())
    print n,m, array

    listA = map(int, raw_input().strip().split())
    setA = set(listA)

    listB = map(int, raw_input().strip().split())
    setB = set(listB)
    print setA, setB

    no_idea(setA, setB, array, n, m)