#include <stdio.h>
int main()
{
	int a;
	scanf("%d", &a);
	printf("%s", (30<=a && 40>=a) || (60<=a && 70>=a) ? "win" : "lose");

	return 0;
}