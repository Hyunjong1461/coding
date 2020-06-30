#include <stdio.h>
int bubble_sort (int size,int arr[]) {
	int i;
	int j;
	int a;
	for (i=1;i<=size;i++){
		for (j=0;j<size-i;j++){
			if(arr[j]>arr[j+1]){
				a=arr[j+1];
				arr[j+1]=arr[j];
				arr[j]=a;
			}
		}
	}
}



int main(){
	int num;
	scanf("%d",&num);
	
	int arr[num];
	int i=0;
	for(i=0;i<num;i++){
		int asd;
		scanf("%d",&asd);
		arr[i]=asd;
	}
	int minvalue=9999999999;
	int maxvalue=-999999999;
	int j=0;
	for (j=0;j<num;j++){
		if (arr[j]<minvalue){
			minvalue=arr[j];
		}
		if (arr[j]>maxvalue){
			maxvalue=arr[j];
		}
	}
	

	
	printf("%d ",minvalue);
	printf("%d",maxvalue);
}
