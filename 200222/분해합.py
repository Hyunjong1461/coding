def divplus (a,n):
    global visit
    if a==n:

    else:
        for i in range(n):
            if i not in visit:
                visit.append(i)
                minus.append(t[i])
                divplus(a+1,n)
                visit.pop()
                minus.pop()

t=str(input())
n=len(t)
plus=[int(t)]
minus=[]
visit=[]

