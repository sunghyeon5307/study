#include <stdio.h>
int main(){
    char s[100];
    int count=0;
    scanf("%s",&s);
    for(int i=0;;i++){
        if(s[i]!=NULL) count++;
        if(s[i]==NULL) break;
    }
    printf("%d",count);
    return 0;
}