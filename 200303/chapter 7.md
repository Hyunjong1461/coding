# chapter 7. Divide and Conquer 경고

### 분할 정복

- 재귀 개념에 대한 이해를 확실히해야한다.
- 문제 -> 답을 알아내기 너무 힘듬
- -> 부분 문제로 나누어서 해결
- 부분 문제의 답으로 문제를 해결



1. divide : input x를 나눔. x1, x2
2. conquer : f(x1),f(x2) ==a,b의 솔루션가 나옴. -> 실제로 동작방식이 어려움.
3. combine: a,b의 솔루션을 통해서 x의 솔루션을 구함.



?-> conquer에서 또 1,2,3이 나눠질 수 있음.

이렇게 되면 문제를 해석하기 어려움.

![분할정복](C:\Users\USER\Desktop\코딩모음\200303\분할정복.PNG)



### EX) 1부터 8까지의 합



![1부터 8까지의 합](C:\Users\USER\Desktop\코딩모음\200303\1부터 8까지의 합.PNG)





### 정렬 알고리즘

- 선택 정렬

- 삽입정렬

- #### 합병 정렬

Divide -> 리스트를 반으로 바눈다

Conquer 왼쪽과 오른쪽을 각각 정렬한다.

combine 두개를 하나로 합친다. 하지만 두개의 리스트를 다시 비교해서 하나로 만들어야한다.

--> dfs처럼 모두 나눠준 다음에, 정렬을 시켜준다.



#### 퀵 정렬

- 합병 정렬과 달리 divide 단계가 핵심.

- #### Partition

  - pivot을 기준으로 작은값은 왼쪽으로, 큰값은 오른쪽으로

- Divide - 어떤 피봇을 기준으로 정렬

- conquer 왼쪽과 오른쪽을 각각 순서대로 정렬

- combine에서는 할 일이 없다.



마지막 것을 pivot으로 삼는것 -> 왼쪽과 오른쪽을 정렬! -> 반복

basecase =>pivot의 양 옆의 갯수가 1개이면 멈춘다.

Partition 함수 설명

- 퀵정렬에서 가장 어려운 부분
- 기준점보다 작은값은 왼쪽에, 기준점보다 큰값은 오른쪽에
- pivot-기준점
- small =pivot보다 작음
- big = pivot보다 큼
- unknown = pivot과 비교해보지 않은 곳
- i로 체크를 하면서 넘어가면서 small그룹과 big그룹을 나눠준다.

```python
def partition (my_list,start,end):
    p=end
    start=small
    b=Big[0]
    i=unknown[0]
```





