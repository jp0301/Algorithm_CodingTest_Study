n, m = map(int, input().split())

result = 0

for i in range(n):  # 행의 개수 만큼 반복문 받고
    data = list(map(int, input().split()))  # 한 줄 씩 입력 받고

    min_value = min(data)  # 그 중 제일 작은 수를 찾는다.
    result = max(result, min_value)  # 작은 수들 중에서 큰 수를 찾는다.

print(result)
