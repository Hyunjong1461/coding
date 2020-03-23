t=int(input())
sachic=['+','*','-','/','.']
for tc in range(1,t+1):
    _list=list(map(str,input().split()))

    for i in range(len(_list)):
        if _list[i] not in sachic:
            _list[i]=int(_list[i])
    # print(_list)
    stack = []
    for j in range(len(_list)):
        stack.append(_list[j])
        if _list[j] in sachic:
            if _list[j]=='+':
                try:
                    a=stack[-3]+stack[-2]
                    stack.pop()
                    stack.pop()
                    stack[-1] = a
                except:
                    print('#{} error'.format(tc))

            if _list[j]=='*':
                try:
                    a = stack[-3] * stack[-2]
                    stack.pop()
                    stack.pop()
                    stack[-1] = a
                except:
                    print('#{} error'.format(tc))

            if _list[j] == '-':
                try:
                    a = stack[-3] - stack[-2]
                    stack.pop()
                    stack.pop()
                    stack[-1] = a
                except:
                    print('#{} error'.format(tc))


            if _list[j] == '/':
                try:
                    a =stack[-3] //stack[-2]
                    stack.pop()
                    stack.pop()
                    stack[-1] = a
                except:
                    print('#{} error'.format(tc))
            if _list[j]=='.':

                break

            # print(stack)
    if len(stack)==2:
        print('#{} {}'.format(tc,int(stack[0])))