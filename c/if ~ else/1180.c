#include <stdio.h>
int main() 
{
    int num, a, b;
    scanf("%d", &num);
    a = num/10;
    b = num%10;
    num = (b*10+a)*2;
    if(num>=100)
    {
        num = num-100;
        if(num<=50) printf("%d\n%s", num, "GOOD");
        else printf("%d\n%s", num, "OH MY GOD");
    }
    else
    {
        if(num<=50) printf("%d\n%s", num, "GOOD");
        else printf("%d\n%s", num, "OH MY GOD");
    }
    
    return 0;
}