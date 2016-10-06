def frequency(string):
    freq = {}
    for i in string:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq

def characters_to_delete(a, b, n):
       
  return (a-n) + (b-n) 
  
def number_needed(a, b):

    ac = frequency(a)
    bc = frequency(b)
    common_length = 0
    for key,value in ac.iteritems():
        if key in bc:
            bcount = bc[key]
        else:
            bcount = 0

        if bcount < value:
          f = bcount
        else:
          f = value

        common_length += f

    return characters_to_delete(len(a), len(b), common_length)
            
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
