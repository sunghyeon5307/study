#include <stdio.h>
int main(){
    int n,m,a,b;
    scanf("%d %d",&n,&m);
    int arr[n];
    for(int i=0;i<n;i++) arr[i]=i+1;
    for(int i=0;i<m;i++){
        scanf("%d %d",&a,&b);
        int num = arr[a-1];
        arr[a-1]=arr[b-1];
        arr[b-1]=num;
    }
    for(int i=0;i<n;i++) printf("%d ",arr[i]);
}