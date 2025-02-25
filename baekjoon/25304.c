#include <stdio.h>
int main() {
    int x,n,a,b,sum=0,total=0;
    scanf("%d\n%d",&x,&n);
    for(int i=0;i<n;i++){
        scanf("%d %d",&a,&b);
        sum=a*b;
        total+=sum;
    }
    if(total==x) printf("Yes");
    else printf("No");
    
}