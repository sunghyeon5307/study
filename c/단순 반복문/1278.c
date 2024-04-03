#include <stdio.h>
int main()
{
    int n=0;
    int m=0;
    scanf("%d", &n);
    while(n != 0)
    {
        n /= 10;
        m ++;
    }
    printf("%d", m);
    return 0;
}
