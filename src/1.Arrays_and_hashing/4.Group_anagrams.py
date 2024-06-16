# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dict = {}
    for str in strs:
        charArray = list(str)
        charArray.sort()
        key = "".join(charArray)
        if key in dict:
            dict[key].append(str)
        else:
            dict[key] = [str]
    result = []
    for key in dict:
        result.append(dict[key])
    return result