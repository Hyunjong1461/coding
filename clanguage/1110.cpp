#include <stdio.h>

int main(){
	int num;
	int num1;
	int num2;
	scanf("%d",&num);
	num1=num;
	int count = 0;
	
	int num3;
	while (1)
	{
		num2=(num%10)*10+(num/10+num%10)%10;
		count++;
		if (num2==num1){
			break;
		}
		num=num2;
	}
	printf("%d",count);
}
