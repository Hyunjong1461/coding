T = int(input())
for TC in range(1, T+1):
    N, value = map(str, input().split())
    N = int(N)
    result = ''
    for i in range(N):
        val = value[i]

        if val == 'A':
            val = 10
        elif val =='B':
            val = 11
        elif val =='C':
            val = 12
        elif val =='D':
            val = 13
        elif val =='E':
            val = 14
        elif val =='F':
            val = 15
        else:
            val = int(val)

        for j in range(3,-1,-1):
            if val & (1<<j):
                result += '1'
            else:
                result += '0'

    print('#{} {}'.format(TC,result))