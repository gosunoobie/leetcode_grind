# top k frequent elements - medium

#class Solution:
#    def topKFrequent(self, nums, k):
#        num_dict = {}
#        for num in nums:
#            if num in num_dict:
#                num_dict[num] += 1
#            else:
#                num_dict[num] = 1
#        sorted_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
#        res = list(sorted_dict.keys())
#        return res[0:k]

class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n,c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
