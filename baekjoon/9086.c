#include <stdio.h>
#include <string.h>
int main(){
    int n;
    char s[1000];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%s",&s);
        int len=strlen(s);
        printf("%c%c\n",s[0],s[len-1]);
    }
    return 0;
}