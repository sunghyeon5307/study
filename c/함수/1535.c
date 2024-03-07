#include <stdio.h>

int n, d[110];

int f()
{
	int ans, mx=0;
	while(n--)
	{
		if(d[n]>=mx)
		{
			mx = d[n];
			ans = n + 1;
		}
	}
	return ans;
}
int main()
{
  scanf("%d", &n);

  for(int i=0; i<n; i++)
    scanf("%d", &d[i]);

  printf("%d", f());
  return 0;
}
