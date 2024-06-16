# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)