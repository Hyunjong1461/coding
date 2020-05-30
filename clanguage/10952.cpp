#include <stdio.h>

int main(){
	int num1;
	int num2;
	int flag =1;
	while(flag=1){
		
		scanf("%d %d",&num1,&num2);
		if (num1==0 && num2==0){
			break;
		}
		printf("%d\n",num1+num2);
		
	}
}
