alist=[]
blist=[]
for i in range(3):
    t=int(input())
    alist.append(t)
for i in range(2):
    t=int(input())
    blist.append(t)
print(min(alist)+min(blist)-50)