public class Solution
{
    public bool hasDuplicate(int[] nums)
    {
        Dictionary<int, bool> dict = new Dictionary<int, bool>();
        foreach (int num in nums)
        {
            if (dict.ContainsKey(num))
            {
                return true;
            }
            dict.Add(num, true);
        }
        return false;
    }
}