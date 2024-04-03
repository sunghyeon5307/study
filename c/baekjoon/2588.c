#include <stdio.h>
int main() 
{
    int a, b, one, two, three, result;
    scanf("%d\n%d", &a, &b);
    one = (b/100)*a;
    two = ((b%100)/10)*a;
    three = (b%10)*a;
    result = a*b;
    printf("%d\n%d\n%d\n%d", three, two, one, result);
    return 0;
}