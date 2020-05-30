#include <stdio.h>

int main(){
	int num1;
	int num2;
	
	scanf("%d %d",&num1,&num2);
	
	int num3;
	int i=0;
	for(i=0;i<num1;i++){
		scanf("%d",&num3);
		if(num3<num2){
			printf("%d ",num3);
		}
	}
}
