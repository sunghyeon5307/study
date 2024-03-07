#include <stdio.h>
int main(){
    int i,n,arr[100],f,r=0;
    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }scanf("%d", &f);
    for(i=0;i<n;i++){
        if(arr[i]==f) r+=1;
    }printf("%d", r);
    return 0;
}