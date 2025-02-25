#include <stdio.h>
int main(){
    int n,m,a,b,c;
    scanf("%d %d",&n,&m);
    int arr[n];
    for(int i=0;i<n;i++) arr[i]=0;
    for(int i=0;i<m;i++){
        scanf("%d %d %d",&a,&b,&c);
        for(int j=a-1;j<b;j++){
            arr[j]=c;
        }
    }
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}