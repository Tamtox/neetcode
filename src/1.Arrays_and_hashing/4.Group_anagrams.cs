public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> dict = new Dictionary<string, List<string>>();
        foreach(string str in strs)
        {
            char[] charArray = str.ToCharArray();
            Array.Sort(charArray);
            string key = new string(charArray);
            if(dict.ContainsKey(key))
            {
                dict[key].Add(str);
            }
            else
            {
                dict.Add(key, new List<string>{str});
            }
        }
        IList<IList<string>> result = new List<IList<string>>();
        foreach(KeyValuePair<string, List<string>> entry in dict)
        {
            result.Add(entry.Value);
        }
        return result;
    }
}