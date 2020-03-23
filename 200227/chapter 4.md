# chapter 4. 재귀함수

#### 재귀 (Recursion)

- 인셉션 영화를 보면 꿈안의 꿈, 꿈안의 꿈 반복 -> 재귀의 예시
- 제귀함수 자기자신을 호출하는 함수



```python
def countdown(n):
    if n>0:
        print(n)
        countdown(n-1)
countdown(4)
```

4,3,2,1 을 출력하고 빠져나옴.

![image-20200227174802411](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200227174802411.png)

그리고 0이 끝났기 때문에, 1도 끝나고, 2도 끝나고, 3도 끝나고, 4도 끝나게되어 최종적으로 끝난다.





#### 팩토리얼(Factorial)

- n! = 1 * 2* ...*(n-1) *n
- 예외) 0! =1

재귀적으로 문제를 푼다는 것 = 같은 형태의 더 작은 문제를 풀고(부분문제)

= 부분문재의 답을 이용하여 기존 문제를 푸는 것



5! = 1 * 2 * 3 * 4 *5 = 120

​				4! = 1 * 2 * 3 * 4 =24

​							3! = 1* 2* 3 =6

​									 2! = 1*2

​											  1! = 1

​													 0!



![image-20200227175443684](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200227175443684.png)

base case와 recursive case 모두 생각해야 함.(재귀문제를 풀 때)



![image-20200227175848946](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20200227175848946.png)



1. 1이 return = factorial(0)

2.  factorial(0)*1=factorial(1)

3.  factorial(1)*2=factorial(2)

4.  factorial(2)*3=factorial(3)

5.  factorial(3)*4=factorial(4)

   -------끝-------



#### 재귀함수 vs 반복문

##### 반복문으로 풀 수 있는 문제는 재귀함수로 풀 수 있고, 또한, 재귀함수로 풀 수 있는 문제는 반복문으로도 풀 수 있다.

재귀함수의 단점 -> 함수의 내부적인 반복 동작을 알아야 함. ->call stack에 저장함.

재귀가 많아지면서 call stack이 쌓이다 보면 메모리에 문제가 생김.

=stackoverflow



재귀함수가 좋을 때 -> 훨씬 깔끔할 때, 효율적일 때가 있음.











