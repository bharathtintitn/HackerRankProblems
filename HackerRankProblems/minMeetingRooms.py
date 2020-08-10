import pdb

class Solution(object):

    def minMeetingRooms(self, intervals):


        if not intervals:
            return 0

        intervals = sorted(intervals)
        print intervals

        start = intervals[0][0]
        end =  intervals[0][1]
        index = 1
        count = [(start, end)]
        pdb.set_trace()
        while index < len(intervals):
            #pdb.set_trace()
            i = 0
            to_add = False
            print "count:{}, i:{}, index:{}".format(count, i, index)
            while i < len(count) and index < len(intervals):
                s, e = count[i][0], count[i][1]
                if e <= intervals[index][0]:
                    to_add = False
                    count[i] = (intervals[index][0], intervals[index][1])
                    index += 1
                    break
                else:
                    i += 1
                    to_add = True
            print to_add
            if to_add:
                new_start, new_end  = intervals[index][0], intervals[index][1]
                count.append((new_start, new_end),)
                index += 1
                count = sorted(count)

        print count
        return len(count)

a = Solution()
#a.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
#a.minMeetingRooms([[7, 10],[2, 4]])
#a.minMeetingRooms([[1,5],[8,9],[8,9]])
a.minMeetingRooms([[15,16],[10,15],[16,25]])
