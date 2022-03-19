# 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    s = ""
    for i in range(1, n+1):
        if(i % 2 == 0):
            s += '박'
        else:
            s += '수'

    return s

print(solution(3))
print(solution(4))

# 한줄 코드
# return "수박"*(n//2) + "수"*(n%2)