#include <stdio.h>

void bubble_sort(int arr[], int count)    // �Ű������� ������ �迭�� ����� ������ ����
{
    int temp;

    for (int i = 0; i < count; i++)    // ����� ������ŭ �ݺ�
    {
        for (int j = 0; j < count - 1; j++)   // ����� ���� - 1��ŭ �ݺ�
        {
            if (arr[j] > arr[j + 1])          // ���� ����� ���� ���� ����� ���� ���Ͽ�
            {                                 // ū ����
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;            // ���� ��ҷ� ����
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
