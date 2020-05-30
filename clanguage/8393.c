#include <stdio.h>

int main(){
	int num;
	scanf("%d",&num);
	
	int t;
	int sum=0;
	for(t=0;t<=num;t++){
		sum+=t;
	}
	printf("%d",sum);
}
