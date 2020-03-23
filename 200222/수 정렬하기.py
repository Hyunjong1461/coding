i = int(input())
s = [0] * 10000
for itr in range(i):
    n = int(input())
    s[n-1] += 1
for idx in range(10000):
    for itr in range(s[idx]):
        print(idx+1)