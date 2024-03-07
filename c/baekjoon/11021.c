#include <stdio.h>
int main(){
    int a,b,t;
    scanf("%d",&t);
    for(int i=1;i<t+1;i++){
        scanf("%d %d", &a, &b);
        printf("%s%d%s %d\n", "Case #", i,":", a+b);
    }
    return 0;
}