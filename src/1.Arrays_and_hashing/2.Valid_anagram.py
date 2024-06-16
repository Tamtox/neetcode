# https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hashset = set()
    dictS = {}
    for c in s:
        if c in dictS:
            dictS[c] += 1
        else:
            dictS[c] = 1
        hashset.add(c)
    dictT = {}
    for c in t:
        if c in dictT:
            dictT[c] += 1
        else:
            dictT[c] = 1
    for c in hashset:
        if c not in dictT or dictT[c] != dictS[c]:
            return False
        valueT = dictT[c]
        valueS = dictS[c]
        if valueT != valueS:
            return False
    return True