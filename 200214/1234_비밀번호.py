import sys;
sys.stdin = open('password.txt', 'r')

# 우선 앞뒤가 같다면 -1로 리스트를 다 바꿈
def passmode (ans):
    while 1:
        for i in range(len(ans) - 1):
            for j in range(0,len(ans)//2):

                if i - j >= 0 and i + j + 1 < len(ans): # 받은 리스트의 범위 설정
                    if ans[i]==ans[i+1]: # 만약에 앞과 뒤가 같다면
                        if ans[i - j] == -1: # 그리고 그 값이 -1이 아니라면 ( -1로 리스트를 다 바꿔서 -1도 바꿔주면 안되기 때문에 설정했음) -> 반복문 멈추기
                            break
                        if ans[i - j] != ans[i + j + 1]: # 그 다음 앞과 뒤가 다르다면ex)7889면 반복문 멈추기
                            break
                        if ans[i - j] == ans[i + j + 1]: # 앞과 뒤가 같으면 ex 8998 이면 99먼저 -1해서 8-1-18되고 그다음에 8 을 -1로 바꿈
                            ans[i-j] = -1
                            ans[i+j + 1] = -1
        else:
            break
    a=[]
    for i in range(len(ans)):
        if ans[i] == -1: #-1인 것은 리스트에서 제외
            continue
        else:
            a.append(ans[i]) #첫번째 제외하기 성공
    for j in range(len(a)-1):
        if a[j]!=a[j+1]: # 만약에 1회 반복한 리스트에 함수를 돌려야 하면 재귀함수로 다시 돌려주기
            continue
        else :
            return passmode(a)
    return a



for tc in range(1,11):
    que=list(map(str,input().split()))
    T=que[0]
    que=list(map(int,str(que[1])))
    # 미지수 받는거
    print('#{}'.format(tc), end = ' ')
    a=passmode(que)# 함수 쓰는거
    for i in range(len(a)):
        print('{}'.format(a[i]),end = '')
    print()

