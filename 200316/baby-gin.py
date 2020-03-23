def babygin(arr):
    arr=sorted(arr)
    i=0
    while 1:
        if len(arr)==0:
            print('triplet')
            return
        elif arr[i]==arr[i+1]==arr[i+2]:
            arr.pop(i)
            arr.pop(i)
            arr.pop(i)
        else:
            break
    i=0
    while 1:
        if len(arr)==0:
            print('triplet')
            return
        elif arr[i+2]-arr[i+1]==1 and arr[i+1]-arr[i]==1:
            arr.pop(i)
            arr.pop(i)
            arr.pop(i)
        elif len(arr)!=0:
            print('asd')
            return



str1=[6,6,7,7,6,7]
str2=[0,5,4,0,6,0]
str3=[1,0,1,1,2,3]
babygin(str1)
babygin(str2)
babygin(str3)
