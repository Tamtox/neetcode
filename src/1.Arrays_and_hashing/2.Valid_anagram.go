// https://leetcode.com/problems/valid-anagram/description/
// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:
// Input: s = "rat", t = "car"
// Output: false
// Constraints:
//     1 <= s.length, t.length <= 5 * 104
//     s and t consist of lowercase English letters.
// Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

package main


func isAnagram(s string, t string) bool {
    if(len(s) != len(t)) {
        return false
    }
    set1:= make(map[rune]int)
    for _, char := range s {
        set1[char]++
    }
    set2:= make(map[rune]int)
    for _, char := range t {
        set2[char]++
    }
    for key, value := range set1 {
        if set2[key] != value {
            return false
        }
    }
    return true
}