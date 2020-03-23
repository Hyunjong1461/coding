def cal(arr):
    operator = '(+*'
    stack = []
    new_line = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            new_line.append(arr[i])
        else:
            if arr[i] == '(':
                stack.append(arr[i])
            elif arr[i] == '+':
                while 1:
                    if len(stack) == 0 or stack[-1] == '(':
                        stack.append(arr[i])
                        break
                    else:
                        new_line.append(stack.pop())
            elif arr[i] == '*':
                while 1:
                    if len(stack) == 0 or stack[-1] == '+' or stack[-1] == '(':
                        stack.append(arr[i])
                        break
                    else:
                        new_line.append(stack.pop())
            elif arr[i] == ')':
                while 1:
                    if len(stack) == 0 or stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        new_line.append(stack.pop())
    return new_line


def calculate(line):
    stack = []
    for i in line:
        if i == '+':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) + int(b))
        elif i == '*':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a) * int(b))
            else:
                return 'error'
        else:
            stack.append(i)
    if len(stack) == 1:
        return stack.pop()





for tc in range(1, 11):
    n = int(input())
    line = input()

    arr = []
    for i in line:
        arr.append(i)



    ans = cal(line)
    print('#{} {}'.format(tc, calculate(ans)))