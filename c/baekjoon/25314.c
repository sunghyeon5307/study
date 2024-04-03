#include <stdio.h>
int main(){
    int i,n;
    char result[100];
    scanf("%d", &n);
    n/=4;
    for(i=0;i<n;i++){
        printf("%s ", "long");
    }printf("%s", "int");
    return 0;
}