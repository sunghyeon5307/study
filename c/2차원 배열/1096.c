#include <stdio.h>
int main() {
    int n,x,y,i,j;
    int arr[20][20]={};
    scanf("%d", &n);
    for(i=1;i<=n;i++) {
        scanf("%d %d", &x, &y);
        arr[x][y]=1;
    }
    for(i=1;i<=19;i++) {
        for(j=1;j<=19;j++)
        {
            printf("%d", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}