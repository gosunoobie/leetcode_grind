# top k frequent elements - medium

class Solution:
    def topKFrequent(self, nums, k):
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        sorted_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
        res = list(sorted_dict.keys())
        return res[0:k]
