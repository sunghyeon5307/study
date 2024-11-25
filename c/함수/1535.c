#include <stdio.h>

int f() {
	int n, a[10], max=0, index=0;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &a[i]);
		if(max<a[i]){
			max=a[i];
			index=i+1;
		}	
	}
	return index;
}
int main() 
{
	printf("%d", f());
	return 0;
}