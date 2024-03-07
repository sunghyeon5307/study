#include <stdio.h>
int main() 
{
    int num=0;
    int i,sum=0;
    scanf("%d", &num);
    for(i=1; sum<num;i++)
    {
        sum=sum+i;
    }
    printf("%d\n", i-1);
    return 0;
}