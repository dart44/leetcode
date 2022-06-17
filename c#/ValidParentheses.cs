namespace ValidParentheses;

public class Solution
{
  public bool IsValid(string s)
  {
    if (string.IsNullOrWhiteSpace(s))
      return true;

    Dictionary<char, char> dict = new Dictionary<char, char>();
    Stack<char> stack = new Stack<char>();

    dict.Add(')', '(');
    dict.Add('}', '{');
    dict.Add(']', '[');

    foreach (var c in s)
      if (c == ')' || c == '}' || c == ']')
      {
        if (stack.Count > 0 && stack.Peek() == dict[c])
          stack.Pop();
        else
          return false;
      }
      else
        stack.Push(c);

    return stack.Count == 0;
  }
}


// public static class Program
// {
//   public static void Main(string[] args)
//   {
//     Solution s = new Solution();
//     Console.WriteLine(s.IsValid("()")); // true
//     Console.WriteLine(s.IsValid("()[]{}")); // true
//     Console.WriteLine(s.IsValid("(]")); // false
//     Console.WriteLine(s.IsValid("([)]")); // false
//     Console.WriteLine(s.IsValid("{[]}")); // true
//   }
// }

