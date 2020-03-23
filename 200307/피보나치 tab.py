def fib_tab(n):
    # 코드를 작성하세요.
    new = 0
    old1 = 1
    old2 = 1
    if n==1:
        return old1
    elif n==2:
        return old2
    else:
        i=2
        while 1:
            if i==n:
                break
            else:
                i+=1
                new=old1+old2
                old1 = old2
                old2 = new
    return new

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))