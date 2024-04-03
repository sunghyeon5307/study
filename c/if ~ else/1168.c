# include <stdio.h>
int main()
{
    int birth, gender, c, a, b, result1, result2;
    scanf("%d %d", &birth, &gender);
    c = birth/10000;
    if(gender == 1 || gender == 2)
    {
        a = 1900+c;
        result1 = 2012-a+1;
        printf("%d",result1);
    }
    else
    {
        b=2000+c;
        result2 = 2012-b+1;
        printf("%d", result2);
    }
    return 0;
}