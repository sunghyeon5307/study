#include <stdio.h>
int main()
{
    int age, result=0, a=0;
    scanf("%d", &age);
    a = 2012-age+1;
    if(2000>a)
    {
        result = a%1900;
        printf("%d %d", result, 1);
    }
    else
    {
        result = a%2000;
        printf("%d %d", result, 3);
    }
}