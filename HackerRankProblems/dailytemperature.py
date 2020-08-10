import pdb

class Solution(object):

    def dailyTemperatures(self, T):

        stack = []
        result = []
        index = len(T) - 1
        pdb.set_trace()
        while index >= 0:

            temp = T[index]
            if stack:
                while stack:
                    top = stack[len(stack)-1]
                    if top[0] > temp:
                        stack.append((temp, index))
                        result.append(top[1] - index)
                        break
                    else:
                        p = stack.pop()
                else:
                    stack.append((temp, index))
                    result.append(0)
            else:
                stack.append((temp, index))
                result.append(0)

            index -= 1
        if result:
            r = map(int, reversed(result))
            print "result:", r
            return r
        return result

a = Solution()
a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])

