// https://leetcode.com/problems/group-anagrams/
// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
// Example 1:
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:
// Input: strs = [""]
// Output: [[""]]
// Example 3:
// Input: strs = ["a"]
// Output: [["a"]]
// Constraints:
//     1 <= strs.length <= 104
//     0 <= strs[i].length <= 100
//     strs[i] consists of lowercase English letters.


func sortString(str string) string {
    runeStr:=[]rune(str)
    sort.Slice(runeStr, func(i,j int) bool {
        return runeStr[i] < runeStr[j]
    })
    return string(runeStr)
}

func groupAnagrams(strs []string) [][]string {
    anagrams := make(map[string][]string)
    for _, str := range strs {
        key:= sortString(str)
        if _, ok := anagrams[key]; !ok {
            anagrams[key] = []string{str}
        } else {
            anagrams[key] = append(anagrams[key], str)
        }
    }
    result:= make([][]string, 0)
    for _, v := range anagrams {
        result = append(result, v)
    }
    return result
}