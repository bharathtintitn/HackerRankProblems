'''
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Ex 1:
    Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
'''
import pdb
from typing import List
from collections import defaultdict

class Solution(object):

    def minOperations(self, logs: List[str]) -> int:
        '''Return length of tree.'''
        stack = []
        self.dfs(logs, 0, stack)
        print(stack)
        return len(stack)


    def dfs(self, logs, index, stack):

        if index >= len(logs):
            return

        node = logs[index]
        print("node:", node)
        if node == '../':
            if len(stack) > 0:
                stack.pop()
            return self.dfs(logs, index+1, stack)

        if node == './':
            return self.dfs(logs, index+1, stack)

        else:
            stack.append(node)
            return self.dfs(logs, index+1, stack)

        return

a = Solution()
a.minOperations(["d1/","d2/","../","d21/","./"])
a.minOperations(["d1/","d2/","./","d3/","../","d31/"])
a.minOperations(["d1/","../","../","../"])
