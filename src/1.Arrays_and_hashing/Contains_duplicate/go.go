package main

func containsDuplicate(nums []int) bool {
    hashmap:= make(map[int]int)
    for _, num := range nums {
        if hashmap[num] == 1 {
            return true
        } else {
            hashmap[num] = 1
        }
    }
    return false
}