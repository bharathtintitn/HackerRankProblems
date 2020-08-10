from itertools import permutations



if __name__ == "__main__":

    hash_map = {} 
    string = raw_input().split()
    for i in xrange(1, len(string)):
        temp = list(map("".join, permutations(string, r=i)))
        for text in temp:

