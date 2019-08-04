#include<stdio.h>
#include<math.h>
void main(){

    int a, b, c;
        printf("Write the value of a:");
    scanf("%d", &a);
        printf("Write the value of b:");
    scanf("%d", &b);
        printf("Write the value of c:");
    scanf("%d", &c);

    double xOne, xTwo, midSqrt, result;

    midSqrt = (b*b)-4*a*c;
    midSqrt = sqrt(midSqrt);

    xOne = (-b + midSqrt) / (2 * a);
    xTwo = (-b - midSqrt) / (2 * a);

    printf("%.2lf\n", midSqrt);
    printf("%.2lf\n", xOne);
    printf("%.2lf\n", xTwo);


    if((a*xOne*xOne+b*xOne+c) == 0 && (a*xTwo*xTwo+b*xTwo+c) == 0){
        printf("The valid value of x for the equation is: %.2lf and %.2lf",
        xOne, xTwo);
    }
    else if((a*xTwo*xTwo+b*xTwo+c) == 0)
    {
        printf("The valid value of x for the equation is: %.2lf", xTwo);
    }
    else{
        printf("The valid value of x for the equation is: %.2lf", xOne);
    }
}
