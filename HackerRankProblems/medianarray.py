import pdb

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            m, n  = len(nums2), len(nums1)
            a, b = nums2, nums1
        else:
            m, n  = len(nums1), len(nums2)
            a, b = nums1, nums2

        start, end = 0, m
        partitionA = (start+end+1)/2
        partitionB = (m+n+1)/2 - partitionA

        while start <= end:
            print "start:{}, end:{}, partA:{}, partB:{}".format(start, end, partitionA, partitionB)
            print "partA:", a[partitionA-1]
            print "partB:", b[partitionB-1]
            if (partitionA == 0 or partitionB == n or a[partitionA-1] <= b[partitionB]) and (partitionB == 0 or partitionA == m or a[partitionA] >= b[partitionB-1]):
                if partitionA == 0:
                    maxLeft = b[partitionB-1]
                elif partitionB == 0:
                    maxLeft = a[partitionA-1]
                else:
                    maxLeft = max(b[partitionB-1], a[partitionA-1])

                if partitionA == m:
                    maxRight = b[partitionB]
                elif partitionB == n:
                    maxRight = a[partitionA]
                else:
                    maxRight = max(b[partitionB], a[partitionA])

                if (m+n)%2 == 0:
                    return (float)(maxLeft+maxRight)/2
                return (float)(maxLeft)


            elif a[partitionA-1] > b[partitionB]:
                end = partitionA - 1
            else:
                start = partitionA + 1

            partitionA = (start+end+1)/2
            partitionB = (m+n+1)/2 - partitionA
            print "Last partA:{}, partB:{}".format(partitionA, partitionB)

        return 0.0

a = Solution()
print a.findMedianSortedArrays([1, 3], [2])
print a.findMedianSortedArrays([1, 2], [3, 4])
