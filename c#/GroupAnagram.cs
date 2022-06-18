// namespace GroupAnagram;

// public class Solution
// {
//   public IList<IList<string>> GroupAnagrams(string[] strs)
//   {
//     Dictionary<string, IList> keyValuePairs = new Dictionary<string, IList>();
//     for (int i = 0; i < strs.Length; i++)
//     {
//       char[] chars = strs[i].ToCharArray();
//       Array.Sort(chars);
//       string sorted_letters = new string(chars);
//       if (keyValuePairs.ContainsKey(sorted_letters))
//       {
//         keyValuePairs[sorted_letters].Add(strs[i]);
//       }
//       else
//       {
//         keyValuePairs.Add(sorted_letters, new List { strs[i] });
//       }
//     }
//   }
// }