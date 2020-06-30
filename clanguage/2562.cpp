#include <stdio.h>


int main(){
	int num =9;

	
	int arr[num];
	int i=0;
	for(i=0;i<num;i++){
		int asd;
		scanf("%d",&asd);
		arr[i]=asd;
	}
	
	int maxvalue=-999999999;
	int count;
	int j=0;
	for (j=0;j<num;j++){
		
		if (arr[j]>maxvalue){
			maxvalue=arr[j];
			count=j;
		}
	}
	


	printf("%d\n",maxvalue);
	printf("%d",count+1);
}

