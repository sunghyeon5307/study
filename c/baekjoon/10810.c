#include <stdio.h>
int main()
{
    int arr[10];
    int a;
    int N=0, M=0; // N:바구니 수, M:공 넣은 수
    int i,j,k;
    scanf("%d %d", &N, &M);
    for(a=0;a>M;a++){
        scanf("%d %d %d", &i, &j, &k);
        for(a=i;a>=j;a++){
            arr[a]=k;
        }
    }
    return 0;
}