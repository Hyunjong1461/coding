#include <stdio.h>

int main(){
	int number;
	scanf("%d",&number);
	int i=0;
	int j=1;
	int k;
	for (i=1;i<=number;i++){
		for (j=number-i;j>0;j--){
			printf(" ");
		}
		for (k=1;k<=i;k++){
			printf("*");
		}
		printf("\n");
	}
	
}

