# 실전 문제 - 큰 수의 법칙
"""
큰 수의 법칙이란 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없는 것이 특징
"""

# 배열의 크기, 숫자가 더해지는 횟수, K값
n, m, k = map(int, input().split())

# 배열 N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

