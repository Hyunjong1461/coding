def func(n, charge, cnt):
    if li[0] <= n + charge:
        print('#{} {}'.format(TC, cnt))
        return

    max_charge = 0
    for i in range(n + 1, n + charge + 1):
        if max_charge < li[i] + i:
            max_idx = i
            max_charge = li[i] + i

    func(max_idx, max_charge - max_idx, cnt + 1)


T = int(input())
for TC in range(1, T + 1):
    li = list(map(int, input().split()))
    func(1, li[1], 0)