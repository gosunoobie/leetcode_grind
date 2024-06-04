# Group anagrams
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs) :
        res =  defaultdict(list)

        for s in strs:
            count = [0] * 26
            # [0] * 26 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            # for example count[97-97] += 1

            res[tuple(count)].append(s)  
            
            # lists cannot used as keys as the keys of a dict need to be immutable(content cannot be changed) and hashable like a tuple 

            # append is possible as it is a defaultdict(list) which returns [] when no value is found for a given key

        return res.values()
            
