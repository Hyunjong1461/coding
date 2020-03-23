import sys;
sys.stdin = open('input.txt','r')


T=int(input()) #테스트 케이스의 갯수
for tc in range(1,T+1):
    N=int(input()) #N개의 버스 노선
    arr=[list(map(int,input().split())) for _ in range(N)] #N개의 줄에 주어진 Ai와 Bi의 리스트
    P=int(input())
    cnt=[[0] for _ in range(P)] #순서대로 주어지는 C 정류장의 버스 노선 카운팅 용
    for p in range(P): #P개의 줄에 C의 정보를 주어주기 위해 for문 사용
        C=int(input()) #확인할 버스정류장 번호
        for n in range(N): #각각의 노선 정보를 확인하여
            if arr[n][0]<=C<=arr[n][1]: #C번 정류장이 Ai 이상 Bi 이하이면
                cnt[p][0]+=1 #C번 정류장 버스 노선을 한 개씩 증가
    print('#{}'.format(tc), end=' ')
    for p in range(P):
        print('{}'.format(cnt[p][0]), end=' ')
    print()