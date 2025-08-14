class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0 
        r = len(numbers) - 1
        notFound = True
        while notFound:
            if numbers[l] + numbers[r] > target:
                r -= 1
                print(l,r,numbers[l],numbers[r])
                continue
            if numbers[l] + numbers[r] < target:
                l += 1
                print(l,r,numbers[l],numbers[r])
                continue
            if numbers[l] + numbers[r] == target:
                print(l,r,numbers[l],numbers[r],'answer found')
                notFound = False
                return [l+1,r+1]