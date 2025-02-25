#include <stdio.h>
int main(){
    int num[10];
    int count,max=0;
    for(int i=1;i<=9;i++){
        scanf("%d\n",&num[i]);
        if(num[i]>max){
            max=num[i];
            count=i;
        }
    }
    printf("%d\n%d",max,count);
}