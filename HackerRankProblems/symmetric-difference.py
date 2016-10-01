'''
Task 
Given  sets of integers,  and , print their symmetric difference in ascending order. The term 
symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, . 
The second line contains  space-separated integers. 
The third line contains an integer, . 
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

'''


na = int(raw_input().strip())
a = set(map(int, raw_input().strip().split()))

nb = int(raw_input().strip())
b = set(map(int, raw_input().strip().split()))

ar = list(a.difference(b))
br = list(b.difference(a))
print ar , br

ar += br
ar.sort()
for i in ar:
    print i
