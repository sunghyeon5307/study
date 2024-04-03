#include <stdio.h>
int main(){
    int n,i,index,max=0;
    for(i=1;i<10;i++){
        scanf("%d", &n);
        if(n>max){
            max=n;
            index=i;
        }
    }printf("%d\n%d", max, index);
    return 0;
}