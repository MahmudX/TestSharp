using System;
using System.Collections.Generic;
namespace FindSubstring
{
    class Program
    {
        public static void Main()
        {
            string userInput = Console.ReadLine();
            Console.WriteLine(GetSubstring(userInput));
            Console.ReadLine();
        }
        public static string GetSubstring(string fullString)
        {
            char[] mainString = fullString.ToLower().ToCharArray();
            List<char> subCharArr = new List<char>();
            subCharArr.Add(mainString[0]);
            bool identifier = false;
            foreach (var mainChar in mainString)
            {
                foreach (var subChar in subCharArr)
                {
                    if (subChar == mainChar)
                    {
                        identifier = true;
                        break;
                    }
                }
                if (identifier != true)
                {
                    subCharArr.Add(mainChar);
                }
                identifier = false;
            }
            return new string(subCharArr.ToArray());
        }
    }
}
