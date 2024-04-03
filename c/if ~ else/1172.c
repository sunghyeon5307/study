#include <stdio.h>
int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if(a>=b && a>=c) // a가 제일 큼
    {
        if(b>=c)
            printf("%d %d %d", c, b, a);
        else
            printf("%d %d %d", b, c, a);
    }
    else if(b>=a && b>=c) // b가 제일 큼
    {
        if(a>=c)
            printf("%d %d %d", c, a, b);
        else
            printf("%d %d %d", a, c, b);
    }
    else // c가 제일 큼
    {
        if(b>=a)
            printf("%d %d %d", a, b, c);
        else
            printf("%d %d %d", b, a, c);
    }

    return 0;
}