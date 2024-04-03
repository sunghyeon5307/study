#include <stdio.h>
int main()
{
    int score = 0, time = 0, i;
    scanf("%d %d", &time, &score);
    for(i=time;i<90;i++)
    {
        if(time<90)
        {
            score += 1;
            time += 5;
        }
    }
    printf("%d", score);
    return 0;
}