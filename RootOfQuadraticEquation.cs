// mahmudnotes.com

using System;
namespace RootOfQuadraticEquation
{
    class Program
    {
        public static void Main()
        {
        // Introductorty
        
            Console.WriteLine("Calculator for roots of the general quadratic equation.");
            Console.WriteLine("Quadratic equation: ax^2 + bx + c = 0");
            Console.WriteLine();
            
            //Variable declearation

            double a, b, c, xOne, xTwo, midSqrt, resultOne, resultTwo;
            
            // Taking input for a, b and c
            
            Console.Write("Write the value of a: ");
            a = double.Parse(Console.ReadLine());
            Console.Write("Write the value of b: ");
            b = double.Parse(Console.ReadLine());
            Console.Write("Write the value of c: ");
            c = double.Parse(Console.ReadLine());

            midSqrt = (b * b) - (4 * a * c);
            midSqrt = Math.Sqrt(midSqrt);

            xOne = ((-(b) + midSqrt) / (2 * a));
            xTwo = ((-(b) - midSqrt) / (2 * a));

            resultOne = (a * xOne * xOne) + (b * xOne) + c;
            resultTwo = (a * xTwo * xTwo) + (b * xTwo) + c;

            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine("Result for the equation {0}x^2+{1}x+{2} is: ", a, b, c);
            Console.WriteLine("Root 1 x = {0}", Math.Round(xOne, 2));
            Console.WriteLine("Root 2 x = {0}", Math.Round(xTwo, 2));

            if (resultOne == 0)
            {
                PrintResult(xOne);
            }
            else if (resultTwo == 0)
            {
                PrintResult(xTwo);
            }
            else
            {
                PrintResult();
            }
            Console.ReadLine();
        }
        public static void PrintResult(double result)
        {
            Console.WriteLine("Valid root for the given quadratic equation is {0}",
                    Math.Round(result, 2));
        }
        public static void PrintResult()
        {
            Console.WriteLine("Both roots are valid for the given quadratic equation.");
        }

    }
}
