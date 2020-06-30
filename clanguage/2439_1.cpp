#include <stdio.h>

int main(){
	int num;
	scanf("%d",&num);
	
	int i;
	int j,k;
	for(i=1;i<=num;i++){
		for(j=num-i;j>0;j--)
		{
			printf(" ");
		}
		for(k=1;k<=i;k++){
			printf("*");
		}
		printf("\n");
	}
}
