from collections import Counter

def count_deletions(s):
  " number of deletions to make same number of elements "
  if len(s)  == 0:
    return 0

  cnts = list(Counter(s).values())
  cnts.sort(reverse=True)
  deletes = 0
  for i in range(1, len(cnts)):
      while cnts[i] >= cnts[i-1] and cnts[i] > 0: # only delete while count > 0
        cnts[i] -= 1
        deletes += 1
  return deletes


print count_deletions("aaaabbbb")
print count_deletions("eeee")
print count_deletions("example")
print count_deletions("ccaaffddecee")
