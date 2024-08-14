# https://leetcode.com/problems/valid-palindrome/
from math import ceil


class Solution:
    def isPalindrome(self, s: str) -> bool:
        isValid = True
        length = len(s)
        mid = ceil(length / 2)
        for num in range(mid):
            if not s[num].lower() == s[length - num - 1].lower():
                isValid = False
                break
        return isValid
    
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        items = dict()
        for num in nums:
            if num not in items:
                items[num] = 1
                result.append(num)
        return result