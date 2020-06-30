#include <stdio.h>

void bubble_sort(int arr[], int count)    // 매개변수로 정렬할 배열과 요소의 개수를 받음
{
    int temp;

    for (int i = 0; i < count; i++)    // 요소의 개수만큼 반복
    {
        for (int j = 0; j < count - 1; j++)   // 요소의 개수 - 1만큼 반복
        {
            if (arr[j] > arr[j + 1])          // 현재 요소의 값과 다음 요소의 값을 비교하여
            {                                 // 큰 값을
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;            // 다음 요소로 보냄
            }
        }
    }
}

int main(){
	int arr[3];
	
	int i;
	int num;
	for (i=0;i<3;i++){
		scanf("%d",&num);
		arr[i]=num;
	}
	int cider;
	int cola;
	
	int water[2];
	scanf("%d",&cider);
	scanf("%d",&cola);
	
	water[0]=cider;
	water[1]=cola;
	bubble_sort(arr, sizeof(arr) / sizeof(int));
	bubble_sort(water, sizeof(water) / sizeof(int));
	

	int k;
	k=arr[0]+water[0]-50;
	printf("%d",k);
	
}
