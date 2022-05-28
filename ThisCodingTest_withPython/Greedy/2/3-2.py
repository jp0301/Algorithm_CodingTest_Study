# 큰 수의 법칙

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[N - 1]  # 배열 크기 5를 입력했으면 0,1,2,3,4번째 중 가장 큰 수는 4번째
second = data[N - 2]  # 두 번째로 큰 수는 3번째 배열

result = 0

while True:
    for i in range(K):  # 가장 큰 수를 K번 더하기
        if M == 0:  # M이 0이라면 반복문 탈출
            break
        result += first  # 더하고
        M -= 1  # 더할 때마다 1씩 뺀다.

    if M == 0:  # M이 0이라면 반복문 탈출
        break
    result += second  # 두 번재로 큰 수를 한 번 더하기
    M -= 1  # 더할 때마다 1씩 빼기

print(result)
