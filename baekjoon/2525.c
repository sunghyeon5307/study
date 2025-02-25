#include <stdio.h>
int main() {
    int h,n,time;
    scanf("%d %d %d", &h,&n,&time);
    int total=(h*60)+n+time;
    h=(total/60)%24;
    n=total%60;
    printf("%d %d", h,n);
}