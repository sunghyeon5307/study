#include <stdio.h>
int main(){
    int n,i,j,s=0;
    scanf("%d", &n);
    for(i=1;i<n+1;i++){
        s+=1;
        for(j=0;j<s;j++){
            printf("*");
        }printf("\n");
    }
    return 0;
}