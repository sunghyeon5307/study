#include <stdio.h>
int main(){
    int n,x;
    scanf("%d %d",&n,&x);
    int arg[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arg[i]);
        if(arg[i]<x) printf("%d ",arg[i]);
    }
}