#Contains duplicate - Easy

class Solution:
    def containsDuplicate(self, nums):
       track = {}
       for num in nums: 
            track[num] = 1 + track.get(num, 0)

            if(track.get(num ,0)) > 1:
                return True
       return False

""" class Solution:
    def containsDuplicate(self,nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False """
