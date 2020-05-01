T = int(input())

for TC in range(1, T+1):
    num = float(input())
    result = ''
    n = 0
    value = 1
    while 1:

        n+=1
        value /= 2

        if num >= value:
            num -= value
            result += '1'
        else:
            result +='0'
        if num==0:
            print('#{} {}'.format(TC,result))
            break
        if n == 13:
            print('#{} {}'.format(TC, 'overflow'))
            break