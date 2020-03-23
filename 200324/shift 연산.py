a=10 # 1010
print(a<<1) # 10100
print(1<<1) # 1 -> 10 ==2
print(1<<2)
print(20>>1)
print(21>>1)

if 6 & 1: #110 #1 #000 둘다 1일 때만 1로 됨.
    print('홀수')
else:
    print('짝수')
# 비트 연산이 가장 빠름.

print( 0 ^ 1) #xor 둘중에 하나만 1일 때, 1로 반환.
print(1^1)