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

   