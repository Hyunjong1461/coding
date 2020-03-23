# 1 7 19 37 61
# 6 12 18 24
#  6  6  6

N=int(input())

i=0
ans=1
while 1:
    if N<=ans:
        print(i+1)
        break
    else:
        i=i+1
        ans=ans+6*i