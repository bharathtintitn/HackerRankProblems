



a = [2, 3, 5, 7]

def rev(a):
    if len(a) <= 0:
        return 
    item = a.pop(0)
    print "Item:", item
    rev(a)
    a.append(item)
    print "a:"

rev(a)
print a

