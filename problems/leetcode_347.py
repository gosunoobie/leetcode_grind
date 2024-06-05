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

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number in nums
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Create a list of lists to use as buckets for frequency
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: Gather the top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Example usage
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(solution.topKFrequent([1], 1))  # Output: [1]
