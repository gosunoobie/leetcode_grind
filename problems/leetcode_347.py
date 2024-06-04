# top k frequent elements - medium

class Solution:
    def topKFrequent(self, nums, k):
        num_dict = {}
        for num in nums:
            if(num_dict.get(num)):
                num_dict[num] += 1
            else:
                num_dict[num] = 0
        res = list(num_dict.keys())
        return res[0:k]

        
