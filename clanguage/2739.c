#include <stdio.h>

int main()
{
	int number;
	scanf("%d",&number);
	int i=0;
	for(i = 1;i<10;i++){
		printf("%d * %d = %d\n",number,i,number*i);
	}
}

