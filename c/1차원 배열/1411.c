#include <stdio.h>
int main()
{
	int arr[50]={};
	int a, b, j, k;
	scanf("%d", &a);
	for(int i=0; i<a; i++)
	{
		arr[i] = i+1;
	}
	for(j=0; j<a-1; j++)
	{
		scanf("%d", &b);
		arr[b-1] = 0; 
	}
	for(k=0; k<a; k++)
	{
		if(arr[k]!=0)
		{
			printf("%d", arr[k]);
		}
	}	
	return 0;
}

