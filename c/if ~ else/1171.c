#include <stdio.h>
int main()
{
    int grade, class, number;
    scanf("%d %d %d", &grade, &class, &number);
    if(class>=10)
    {
        if(number>=100)
            printf("%d%d%d", grade, class, number);
        else if(100>number && number>10)
            printf("%d%d0%d", grade, class, number);
        else
            printf("%d%d00%d", grade, class, number);
    }
    else
    {
        if(number>=100)
            printf("%d0%d%d", grade, class, number);
        else if(100>number && number>10)
            printf("%d0%d0%d", grade, class, number);
        else
            printf("%d0%d00%d", grade, class, number);
    }
    return 0;
}