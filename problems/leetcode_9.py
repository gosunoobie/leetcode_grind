#is Palindrome - easy
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        rev = list(x)[::-1]
        org = ''.join(rev) 
        return org == x
