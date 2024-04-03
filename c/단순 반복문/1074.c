#include <stdio.h>
int main() 
{
	int a;
	scanf("%d", &a);
	while(1)
	{
		if(a==0)
		break;
		printf("%d\n", a);
		a=a-1;
	}
	return 0;
}
