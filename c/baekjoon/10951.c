#include <stdio.h>
int main(){
    int i=0,a, b;
    while(scanf("%d %d", &a, &b)!=EOF){
        if(a==EOF && b==EOF) break;
        else printf("%d\n", a+b);
    }
    return 0;
}