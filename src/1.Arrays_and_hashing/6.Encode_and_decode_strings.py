# https://leetcode.com/problems/encode-and-decode-strings/
# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

# Constraints:
#     0 <= strs.length < 100
#     0 <= strs[i].length < 200
#     strs[i] contains only UTF-8 characters.


class Solution:
    def encode(self, strs: List[str]) -> str:
      if not strs: return ""
      res = ''
      for str in strs:
        res += res + '/' + str
      return res
    def decode(self, s: str) -> List[str]:
      arr = []
      subStr = ''
      for i in range(len(s)):
        if s[i] == '/':
          arr.append(subStr)
          subStr = ''
        else:
          subStr += s[i]
