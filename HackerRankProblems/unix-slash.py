class Solution(object):
    def simplifyPath(self, path):

        p = path.split('/')
        print "p:", p
        result = []

        while len(p) > 0:
            string = p.pop(0)
            if string == '.':
                continue
            if string == '..':
                if len(result) > 0:
                    remove = result.pop()
                    print "moving up:", remove
                continue
            if string:
                result.append(string)

        ret = "/" + "/".join(result)

        print "ret:", ret
        return ret

a = Solution()
a.simplifyPath("/a//b////c/d//././/..")
a.simplifyPath("/a/../../b/../c//.//")
a.simplifyPath("/a/./b/../../c/")
a.simplifyPath("/home//foo/")
a.simplifyPath("/../")
a.simplifyPath("/home/")
