# Two Sum II - easy

# solution using hashing
#class Solution:
#    def twoSum(self, numbers, target):
#        prevMap = {}
#
#        for index, num in enumerate(numbers):
#            diff = target - num
#            if diff in prevMap:
#                return [prevMap[diff], index + 1]
#            prevMap[num] = index

# soultion using the two pointers
class Solution:
    def twoSum(self, numbers, target):
        l,r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            print(sum)
            print(numbers[l], numbers[r])
            if sum == target:
                return [l + 1, r+1]
            if sum > target:
                r -= 1
            else :
                l += 1 
        

