# C언어 정리파일

1. 입력받는 법

   ```c
   scanf("%d %d",&num1,&num2);
   ```

2. 0<number<99 안됨

   ```c
   if(80<=number && number<=89)
   ```

3. 나머지연산

   ```c
   %
   ```

4. for문

   ```c
   for(i = 1;i<10;i++){
   		printf("%d * %d = %d\n",number,i,number*i);
   	}
   ```

5. while문

   ```c
   while(flag=1){
   		scanf("%d %d",&num1,&num2);
   		if (num1==0 && num2==0){
   			break;
   		}
   		printf("%d\n",num1+num2);
   		
   	}
   //파이썬과 비슷하다.
   ```

6. ##### while로 입력받기

   ```c
   #include <stdio.h>
   
   int main(){
   	int num1;
   	int num2;
   	int flag =1;
   	while(scanf("%d %d",&num1,&num2)==2){
   		
   		printf("%d\n",num1+num2);
   	}
   }
   ```

7. python과 다른점 한가지

   ```c
   #include <stdio.h>
   
   int main(){
   	int num;
   	int num1;
   	int num2;
   	scanf("%d",&num);
   	num1=num;
       //값을 변수하나를 통해서 저장할 수 있음.
   	int count = 0;
   	
   	int num3;
   	while (1)
   	{
   		num2=(num%10)*10+(num/10+num%10)%10;
   		count++;
   		if (num2==num1){
   			break;
   		}
   		num=num2;
           //바뀌는 것을 계속 반영해주기 위해서 사용
   	}
   	printf("%d",count);
   }
   ```

8. bubble_sort

   ```c
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
   ```

   