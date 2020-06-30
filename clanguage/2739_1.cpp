#include <stdio.h>
int main(){
	int num1;
	scanf("%d",&num1);
	
	int i;
	for (i=1;i<10;i++){
		printf("%d * %d = %d\n",num1,i,num1*i);
	}
}
