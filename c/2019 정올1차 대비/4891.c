// 행복 
#include <stdio.h>
int main()
{
	int max=0, min=0, num, score;
	scanf("%d", &num);
	scanf("%d", &score);
	max = min = score;
	for(int i=1; i<num; i++)
	{
		scanf("%d", &score);
		if(max<score)
			max = score;
		if(min>score)
			min = score;	
	}	
	printf("%d",max - min);

	return 0;
}
