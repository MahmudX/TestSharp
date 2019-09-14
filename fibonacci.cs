using System;
using System.Diagnostics;
class Program
{
    static void Main()
    {
    START:


        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();
        Console.WriteLine("Fib {0}: {1}", 30, fib(30));
        stopwatch.Stop();
        Console.WriteLine("Time elapsed: " + stopwatch.Elapsed);

        Console.ReadLine();
        Console.Clear();
        goto START;
    }
    public static double fib(double n)
    {
        if (n == 1)
        {
            return 1;
        }
        else
        {
            n = n * fib(n - 1);
        }
        return n;
    }
}
