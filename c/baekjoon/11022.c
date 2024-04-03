#include <stdio.h>
int main(){
    int t, a, b, i;
    scanf("%d", &t);
    for(i=1;i<t+1;i++){
        scanf("%d %d", &a, &b);
        printf("%s%d%s %d %s %d %s %d\n", "Case #", i, ":", a, "+", b, "=", a+b);
    }
    return 0;
}