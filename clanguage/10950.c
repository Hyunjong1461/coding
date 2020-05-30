#include <stdio.h>

int main(){
	int number;
	scanf("%d",&number);
	int i=0;
	for (i=0;i<number;i++){
		int num1;
		int num2;
		scanf("%d %d",&num1,&num2);
		printf("%d\n",num1+num2);
	}
}
