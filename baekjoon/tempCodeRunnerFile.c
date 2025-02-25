#include <stdio.h>
#include <string.h>
int main(){
    char a[4],b[4];
    char resulta[4],resultb[4];
    scanf("%s %s",a,b);
    for(int i=0;i<strlen(a);i++){
        resulta[i]=a[strlen(a)-1-i];
        resultb[i]=b[strlen(b)-1-i];
    }
    resulta[strlen(a)]='\0';
    resultb[strlen(b)]='\0';
    if(a>b) printf("%s\n",resulta);
    else printf("%s\n",resultb);
    return 0;
}