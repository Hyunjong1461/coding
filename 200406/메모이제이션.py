# 중복된 결과 값을 stack에 저장해서 실행속도를 줄이는 방법
# 피보나치 실행시간을 줄이기가 목적

def fibo(n):
    if n<=2: return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(35))

memo =[0,1,1]+[0]*100

def fibo_memo(n):
    if n<=2: return 1
    if memo[n]:return memo[n]

    memo[n]= fibo_memo(n-1)+fibo_memo(n-2)
    return memo[n]
print(fibo(35))