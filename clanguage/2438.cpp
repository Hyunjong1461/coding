#include <stdio.h>

int main(){
	int number;
	scanf("%d",&number);
	int i=0;
	int j=1;
	for (i=1;i<=number;i++){
		for (j=1;j<=i;j++){
			printf("*");
		}
		printf("\n");
	}
}
