public class Solution {
    public bool IsAnagram(string s, string t) {
      if(s.Length != t.Length) return false;
      HashSet<char> set = new HashSet<char>();
      Dictionary<char, int> dictS = new Dictionary<char, int>();
      foreach(char c in s)
      {
        if(dictS.ContainsKey(c))
        {
          dictS[c]++;
        }
        else
        {
          dictS.Add(c, 1);
        }
        set.Add(c);
      }
      Dictionary<char, int> dictT = new Dictionary<char, int>();
      foreach(char c in t)
      {
        if(dictT.ContainsKey(c))
        {
          dictT[c]++;
        }
        else
        {
          dictT.Add(c, 1);
        }
      }
      foreach(char c in set)
      {
        if(!dictT.ContainsKey(c) || dictT[c] != dictS[c])
        {
          return false;
        }
        int valueT = dictT[c];
        int valueS = dictS[c];
        if(valueT != valueS)
        {
          return false;
        }
      }
      return true;
    }
}
