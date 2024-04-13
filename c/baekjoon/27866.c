#include <stdio.h>
int main() {
  int num;
  char s[1000];
  scanf("%s\n%d", s, &num);
  printf("%c", s[num - 1]);
  return 0;
}