#longestConsecutive - hard

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                length = 0
            # check check until the end of the sequence
                while( n + length) in numSet:
                    length += 1
            # settings the longest if the new length is greater
                longest = max(length, longest)

        return longest
