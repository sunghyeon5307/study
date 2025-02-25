#include <stdio.h>
int main() {
    int n,num,count=0;
    scanf("%d",&n);
    int v[n];
    for(int i=0;i<n;i++){
        scanf("%d",&v[i]);
    }
    scanf("%d",&num);
    for(int j=0;j<n;j++){
        if(v[j]==num) count++;
    }
    printf("%d",count);
}