import pdb

class Solution(object):

    def exclusiveTime(self, n, logs):

        result = [0]*n
        print result
        if not logs:
            return []
        logs_list = []
        for l in logs:
            l = l.split(":")
            logs_list.append([int(l[0]), l[1], int(l[2])])
            #logs_list.append(l.split(":"))
        print logs_list

        logs_list = sorted(logs_list, key=lambda x: x[2])
        print logs_list

        stack = [[-1,"None",0, 0]]
        counter = -1
        curr = -1
        pdb.set_trace()
        for l in logs_list:
            pdb.set_trace()
            top = stack[len(stack)-1]
            if top[0] <> l[0]:
                if l[1] == 'start':
                    top[3] = top[3] + (l[2] - counter)
                    l.append(0)
                    stack.append(l)
                    counter = l[2]
                else:
                        stack.pop()
                        time_taken = top[3] + (l[2]-counter+1)
                        result[l[0]] += time_taken
                        counter = l[2] + 1
            else:
                #time_taken = l[2] - top[2]
                if l[1] == 'start':
                    top[3] = top[3] + (l[2] - counter)
                    counter = l[2]
                else:
                    stack.pop()
                    time_taken = top[3] + (l[2]-counter+1)
                    result[l[0]] += time_taken

                    counter = l[2] + 1

        print "*******"
        print result

#counter start
#counter end

a = Solution()
#print a.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"])
#print a.exclusiveTime(2, ["0:start:0","1:start:2","1:end:9","0:end:6"])
print a.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"])
