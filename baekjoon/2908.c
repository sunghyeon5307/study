#include <stdio.h>
#include <string.h>
#include <stdlib.h>
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
    int A=atoi(resulta);
    int B=atoi(resultb);
    if(A>B) printf("%d",A);
    if(B>A) printf("%d",B);

    return 0;
}