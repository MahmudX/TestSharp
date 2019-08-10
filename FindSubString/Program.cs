using System;
using System.Collections.Generic;
namespace FindSubstring
{
    class Program
    {
        public static List<char> subCharArr = new List<char>();
        public static void Main()
        {
            char[] mainString = Console.ReadLine().ToCharArray();
            subCharArr.Add(mainString[0]);
            bool identifier = false;
            foreach (var mainChar in mainString)
            {
                foreach (var subChar in subCharArr)
                {
                    if (subChar == mainChar)
                    {
                        identifier = true;
                    }
                }
                if (identifier != true)
                {
                    subCharArr.Add(mainChar);
                }
                identifier = false;
            }
            string subString = new string(subCharArr.ToArray());
            Console.WriteLine(subString);
            Console.ReadLine();
        }
    }
}
