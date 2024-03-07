#include <stdio.h>
int main()
{
    int h, m, time;
    scanf("%d %d\n%d", &h, &m, &time);
    time+=m;
    if(time<60) printf("%d %d", h, time);
    else if(time>=60){
        h=h*60;
        time+=h;
        if(time/60>=24) printf("%d %d", (time/60)-24, time%60);
        else printf("%d %d", time/60, time%60);
    }
    return 0;
}