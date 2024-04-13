#include <stdio.h>
#include <string.h>
int main() {
    int i, num;
    char s[100];
    scanf("%d", &num);
    for(i=0; i<num; i++) {
        scanf("%s", s);
        printf("%c%c\n", s[0], s[strlen(s)-1]);
    }
    return 0;
}