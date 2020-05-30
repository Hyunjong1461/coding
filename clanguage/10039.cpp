#include <stdio.h>

int main(){
	int i;
	int x;
	int sum=0;
	for (i=0;i<5;i++){
		scanf("%d",&x);
		if(x<40){
			x=40;
		}
		sum+=x;
	}
	printf("%d",sum/5);
}
