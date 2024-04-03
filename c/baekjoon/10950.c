// #include <stdio.h>
// int main()
// {
//     int t, a, b, i, j;
//     char a1[10], b1[10];
//     scanf("%d", &t);
//     for(i=0;i<t;i++){
//         scanf("%d %d", &a, &b);
//         a1[i]=a;
//         b1[i]=b;
//     }
//     for(j=0;j<t;j++){
//         printf("%d\n", a1[j]+b1[j]);
//     }
//     return 0;
// }
#include <stdio.h>
int main()
{
    int i, t, a, b;
    scanf("%d", &t);
    for(i=0;i<t;i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
    return 0;
}