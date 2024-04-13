#include <stdio.h>
int main()
{
    int num, sum=0;
    char n[100];
    scanf("%d", &num);
    scanf("%s", n);
    for(int i=0; i<num; i++) {
        sum += n[i]-'0';
    }
    printf("%d\n", sum);
    return 0;
}