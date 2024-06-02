public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++)
        {
          int num = nums[i];
          int diff = target - num;
          bool hasDiff = dict.ContainsKey(diff);
          if(hasDiff)
          {
            return new int[]{dict[diff], i};
          }
          if(!dict.ContainsKey(num))
          {
            dict.Add(num, i);
          }
        }
        return new int[]{0,1};
    }
}