#include <stdio.h>

int main(){
	int number;
	scanf("%d",&number);
	int i=0;
	for (i=1;i<=number;i++){
		int num1;
		int num2;
		scanf("%d %d",&num1,&num2);
		printf("Case #%d: %d\n",i,num1+num2);
	}
}
