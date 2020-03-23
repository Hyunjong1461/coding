t=str(input())
ans=[-1]*26
for i in range(len(t)):
    if ans[ord(t[i])-97]==-1:
        ans[ord(t[i])-97]=i
    else:
        continue
for i in ans:
    print(i,end=' ')
