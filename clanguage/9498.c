#include <stdio.h>

int main()
{	
	int number;
	scanf("%d",&number);
	
	if(90<=number && number<=100){
		printf("A");
	}
	else if(80<=number && number<=89){
		printf("B");
	}
	else if(70<=number && number<=79){
		printf("C");
	}
	else if(60<=number && number<=69){
		printf("D");
	}
	else{
		printf("F");
	}
	
}
