# 12928번 약수의 합 문제

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

def solution(n):
    n = int(n)
    sum = 0

    for i in range(1, n+1):
        if(n % i == 0):
            sum += i
    return sum


print(solution(12))
print(solution(5))


# 한줄 코드
# def sumDiv(n):
#       return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
