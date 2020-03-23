import sys;
sys.stdin = open('input.txt','r')

t=int(input())

for i in range(t):
    arr = []
    k = str(input())
    for i in range(len(k)):
        if k[i] == '(':
            arr.append(k[i])
        elif k[i]==')':
            if '(' in arr:
                arr.pop()
            else:
                arr.append(k[i])
    if len(arr)==0:
        print('YES')
    else:
        print('NO')
