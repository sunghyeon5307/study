#include <stdio.h>
int main(){
    int result;
    int arr[7]={1,1,2,2,2,8};
    for(int i=0;i<6;i++){
        scanf("%d",&result);
        printf("%d ",arr[i]-result);
    }
}