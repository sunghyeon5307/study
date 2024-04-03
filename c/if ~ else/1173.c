#include <stdio.h>
int main()
{
    int time, min;
    scanf("%d %d", &time, &min);

    if(min<30) 
    {
        min = min+30;
        time = time-1;
        if(time<0)
        {
            time=23;
        }
        printf("%d %d", time, min);
    }
    else if(min>=30)
    {
        min = min-30;
        printf("%d %d", time, min);
    }
    return 0;
}