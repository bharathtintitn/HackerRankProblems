'''
This is snake and ladder game.
Markov takes out his Snakes and Ladders game and stares at the board, and wonders: If he had absolute control on the die (singular), and could get it to generate any number (in the range ) he desired, what would be the least number of rolls of the die in which he'd be able to reach the destination square (Square Number ) after having started at the base square (Square Number )?

Rules

Markov has total control over the die and the face which shows up every time he tosses it. You need to help him figure out the minimum number of moves in which he can reach the target square (100) after starting at the base (Square 1).

A die roll which would cause the player to land up at a square greater than 100, goes wasted, and the player remains at his original square. Such as a case when the player is at Square Number 99, rolls the die, and ends up with a 5.

If a person reaches a square which is the base of a ladder, (s)he has to climb up that ladder, and he cannot come down on it. If a person reaches a square which has the mouth of the snake, (s)he has to go down the snake and come out through the tail - there is no way to climb down a ladder or to go up through a snake.

Constraints

The board is always of the size  and Squares are always numbered  to .

 
  

  Square number 1 and 100 will not be the starting point of a ladder or a snake. 
  No square will have more than one of the starting or ending point of a snake or ladder (e.g. snake 56 to 44 and ladder 44 to 97 is not possible because 44 has both ending of a snake and a starting of a ladder)

  Input Format

  The first line contains the number of tests, T. T testcases follow.

  For each testcase, the first line contain N(Number of ladders) and after that N line follow. Each of the N line contain 2 integer representing the starting point and the ending point of a ladder respectively.

  The next line contain integer M(Number of snakes) and after that M line follow. Each of the M line contain 2 integer representing the starting point and the ending point of a snake respectively.

  Output Format

  For each of the T test cases, output one integer, each in a new line, which is the least number of moves (or rolls of the die) in which the player can reach the target square (Square Number 100) after starting at the base (Square Number 1). This corresponds to the ideal sequence of faces which show up when the die is rolled. 
  If there is no solution, print -1.

  Sample Input

  2
  3
  32 62
  42 68
  12 98
  7
  95 13
  97 25
  93 37
  79 27
  75 19
  49 47
  67 17
  4
  8 52
  6 80
  26 42
  2 72
  9
  51 19
  39 11
  37 29
  81 3
  59 5
  79 23
  53 7
  43 33
  77 21 
  Sample Output

  3
  5
  Explanation

  For the first test: To traverse the board via the shortest route, the player first rolls the die to get a 5, and ends up at square 6. He then rolls the die to get 6. He ends up at square 12, from where he climbs the ladder to square 98. He then rolls the die to get '2', and ends up at square 100, which is the target square. So, the player required 3 rolls of the die for this shortest and best case scenario. So the answer for the first test is 3.
'''

import pdb
import heapq as q

def create_graph(ladder, snake, ladders, snakes):

    graph = {}

    for i in xrange(1,101):
        temp =[]
        for j in xrange(1, 7):
            if i+j <= 100:
                temp.append(i+j)
        graph[i] = temp

    #print "Graph is "
    #for source, dest in graph.items():
        #print "{}: {}".format(source, dest)


    #print "Update ladders"
    #pdb.set_trace()
    for ladder in ladders:
        start = ladder[0]
        end = ladder[1]
        j = 0
        index = start - 6
        if index <= 0:
            index = 1
        for i in reversed(xrange(index,start)):
            graph[i][j] = end
            j += 1
            #print "{}: {}".format(i, graph[i])

    #print "Update snake"
    for snake in snakes:
        start = snake[0]
        end = snake[1]
        j = 5
        for i in xrange(start-6, start):
            graph[i][j] = end
            j -= 1
            #print "{}: {}".format(i, graph[i])


    dijkstra(graph)

def dijkstra(graph):

    visited = {1: 0}
    path = {1: 0}
    heap = set()
    heap.add(1)
    #pdb.set_trace()
    while heap:
        source = heap.pop()
        nodes = graph[source]
        level = visited[source]
        for node in nodes:
            if node in visited:
                current_level = visited[node]
                if current_level > level + 1:
                    visited[node] = level + 1
                    path[node] = source
            else:
                visited[node] = level + 1
                path[node] = source
                heap.add(node)

    #pdb.set_trace()
    #print path
    print visited[100]

if __name__ == "__main__":

    t = int(raw_input().strip())
    for _ in xrange(t):
        ladder = int(raw_input().strip())
        ladders = []
        for _ in xrange(ladder):
            row = map(int, raw_input().split())
            ladders.append(row)

        #print ladders

        snake = int(raw_input().strip())
        snakes = []
        for _ in xrange(snake):
            row = map(int, raw_input().split())
            snakes.append(row)

        #print snakes

        create_graph(ladder, snake, ladders, snakes)
    #graph = {1: [2,3,4], 2:[3,4,7], 3:[4,5,10],4:[],5:[],6:[],7:[10], 10:[]}
