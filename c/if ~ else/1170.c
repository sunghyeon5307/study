#include <stdio.h>
int main()
{
    int grade, class, number;
    scanf("%d %d %d", &grade, &class, &number);
    if(number<10)
    {
        printf("%d%d0%d", grade, class, number);
    }
    else 
    {
        printf("%d%d%d", grade, class, number);
    }
    return 0;
}