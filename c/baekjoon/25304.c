#include <stdio.h>
int main(){
    int result=0,mul=0,x,n,a,b;
    scanf("%d\n%d", &x, &n);
    for(int i=0;i<n;i++){
        scanf("%d %d", &a, &b);
        mul=a*b;
        result+=mul;
        mul=0;
    }
    if(x==result) printf("Yes");
    else printf("No");
    return 0;
}