import pdb

def IDsOfSongs(rideDuration, songDurations):
    # WRITE YOUR CODE HERE
    target = rideDuration - 30
    hashtable = {}
    result = set()
    for i, j in enumerate(songDurations):
        hashtable[j] = i
    print songDurations, ' ', rideDuration, ' ', target
    print hashtable
    pdb.set_trace()    
    for i, j in enumerate(songDurations):
        print "find:", target - j,  '  ', target, ' ', j
        if hashtable.get(target - j):
            index_1 = hashtable[target-j]
            index_2 = i
            
            if index_2 < index_1:
                result.add((index_2, index_1),)
            result.add((index_1, index_2),)
    
    print result
    max_time = 0
    for k, j in result:
        
        if songDurations[k] > max_time:
            max_time = songDurations[k]
            index_1 = k
            
        if songDurations[j] > max_time:
            max_time = songDurations[k]
            index_1 = j
            
        if index_1 < index_2:
            print "Return:", index_1, ' ', index_2
            return [index_1, index_2]
        print "Return:", index_2, ' ', index_2
        return [index_2, index_1]
       

IDsOfSongs(250, [100,180, 40, 120, 10]) 
