#include <stdio.h>
int main(){
    int i,n,x,arr[10000],r;
    scanf("%d %d", &n, &x);
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
        if(arr[i]<x) printf("%d ", arr[i]);
    }
    return 0;
}