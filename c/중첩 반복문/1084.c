#include <stdio.h>
int main()
{
    int i,j,k;
    int x,y,z;
    scanf("%d %d %d", &i, &j, &k);
    for(x=0; x<i; x++)
    {
        for(y=0;y<j;y++)
        {
            for(z=0; z<k; z++)
            {
                printf("%d %d %d\n", x, y, z);
            }
        }
    }
    printf("%d", i*j*k);
    return 0;
}