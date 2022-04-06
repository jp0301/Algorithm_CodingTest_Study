# 최대공약수와 최소공배수 구하기
# 유클리드 호제법

def solution(n, m):
    a, b = max(n, m), min(n, m)
    t = 1

    while t > 0:
        t = a % b
        a, b = b, t

    answer = [a, int(n * m / a)]
    return answer


print(solution(2, 5))