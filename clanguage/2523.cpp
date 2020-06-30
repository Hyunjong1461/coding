#include <stdio.h>

int main(){
	int num;
	scanf("%d",&num);
	
	int i;
	int j;
	for (i=1;i<=(2*num-1);i++){
		if (i<=num){
			for (j=1;j<=i;j++){		
				printf("*");
			}
		}
		else{
			for(j=2*num-i;j>0;j=j-1){
				printf("*");
			}		
			
		}
		printf("\n");
	}
}
