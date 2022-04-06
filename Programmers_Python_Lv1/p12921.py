# 12921 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    div = set(range(2, n+1))

    for i in range(2, n+1):
        if i in div:
            div -= set(range(2*i, n+1, i)) 

    return len(div)


print(solution(10))
print(solution(5))

# 에라토스테네스의 체
print(set(range(2, 11)))
