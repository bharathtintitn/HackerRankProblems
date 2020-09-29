import pdb

class Solution(object):

    def minDays(self, n: int) -> int:
        print("***********")
        dp = [0]*(n+1)
        print(dp)
        for i in range(1, n+1):
            if i == 1:
                dp[1] = 1
            elif i == 2:
                dp[2] = 1
            elif i == 3:
                dp[3] = 2
            else:
                temp = []
                temp.append(dp[i-1])
                if i%2 == 0:
                    index = int(i/2)
                    temp.append(dp[i-index])
                if i%3 == 0:
                    index = int(2*(i/3))
                    temp.append(dp[i-index])
                print("temp:", temp)
                eat = min(temp)+1
                dp[i] = eat
                print("i:{}, eat:{}, temp:{}, dp:{}".format(i, eat, temp, dp))
        return dp[-1]

a = Solution()
print(a.minDays(1))
print(a.minDays(6))
print(a.minDays(10))
#print(a.minDays(56))
