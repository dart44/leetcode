// See https://aka.ms/new-console-template for more information

namespace CSharp
{
  class Program
  {
    static void Main(string[] args)
    {
      void HelloWorld()
      {
        string hello = "Hello World";
        Console.WriteLine(hello);
        List<int> list = new List<int>() { 1, 2, 3, 4, 5 };
        Console.WriteLine(list[0]);
      }
      HelloWorld();
    }
  }
}