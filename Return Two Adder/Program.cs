using System;
using System.Diagnostics;
using System.Collections.Generic;
class Program
{
    static void Main()
    {
    START:

        string input = Console.ReadLine();
        int k = int.Parse(Console.ReadLine());
        Stopwatch stopwatch = new Stopwatch();
        int firstNumber = 0;
        int secondNumber = 0;
        bool breaker = false;

        stopwatch.Start();

        int[] intArr = Array.ConvertAll(input.Split(' '),
                arTemp => int.Parse(arTemp));
        List<int> numberList = new List<int>();

        foreach (var item in intArr)
        {
            numberList.Add(item);
        }
        //numberList.Sort();
        for (int i = 0; i < intArr.Length - 1; i++)
        {
            int temp = k - numberList[i];
            for (int j = i + 1; j < intArr.Length; j++)
            {
                if (numberList[j] == temp)
                {
                    firstNumber = numberList[i];
                    secondNumber = numberList[j];
                    breaker = true;
                    break;
                }
            }
            if (breaker)
            {
                break;
            }
        }

        stopwatch.Stop();

        if (breaker)
        {
            Console.WriteLine("Result : {0} and {1}", firstNumber, secondNumber);
        }
        else Console.WriteLine("No Match found");
        Console.WriteLine("Time Taken :" + stopwatch.Elapsed);

        Console.ReadLine();
        Console.Clear();
        goto START;
    }
}