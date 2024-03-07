#include <stdio.h>
int main() 
{
	char a;
	while(1)
    {
		scanf("%c", &a);
		printf("%c\n",a);
		if(a=='q')
		break;
	}
	return 0;
}
