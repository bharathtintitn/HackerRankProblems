import sys

def toys(w):
    w = set(w)
    a = 0
    import pdb
    pdb.set_trace()
    while len(w) >0:
        z = min(w)
        a += 1
        w = list(filter(lambda x: x > z + 4, w))
    return a

    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())
    w = list(map(int, raw_input().strip().split(' ')))
    result = toys(w)
    print(result)
