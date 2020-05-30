#include <stdio.h>

int main()
{
	int num1;
	int num2;
	
	scanf("%d",&num1);
	scanf("%d",&num2);
	
	if(num1>0 && num2>0 ){
		printf("1");
	}
	else if(num1<0 && num2>0 ){
		printf("2");
	}
	else if(num1>0 && num2<0 ){
		printf("4");
	}
	else if(num1<0 && num2<0 ){
		printf("3");
	}
}
	
