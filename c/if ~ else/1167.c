#include <stdio.h>
int main() 
{
    int a, b, c, result=0;
    scanf("%d %d %d", &a, &b, &c);
    if(a<=b && a<=c) // a가 가장 작음
    {
        if(b<c)
            result = b;
        else
            result = c;
    }
    else if(b<=a && b<=c) // b가 가장 작음
    {
        if(c<a)
            result = c;
        else
            result = a;
    }
    else if(c<=a && c<=b) // c가 가장 작음
    {
        if(a<b)
            result = a;
        else
            result = b;
    }
    printf("%d", result);
    return 0;
}