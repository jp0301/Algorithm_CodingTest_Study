# 6041. [기초-산술연산] - 정수 2개 입력받아 나눈  나머지 계산하기
a, b = input().split()
print(int(a)%int(b))

# 6042. [기초-값변환] - 실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a, ".2f"))

# 6043. [기초-산술연산] - 실수 2개 입력받아 나눈 결과 계산하기
f1, f2 = input().split()
f3 = float(f1) / float(f2)
print(format(f3, ".3f"))

# 6044. [기초-산술연산] - 정수 2개 입력받아 자동 계산하기
a, b = input().split()
a, b = int(a), int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(float(a)/float(b), '.2f')) # round(a/b, 2)

# 6045. [기초-산술연산] - 정수 3개 입력받아 합과 평균 출력하기
a, b, c = input().split()
d = int(a) + int(b) + int(c)
e = d / 3
print(d, format(e, '.2f'))

# 6046. [기초-비트시프트연산] - 정수 1개 입력받아 2배 곱해 출력하기
a = int(input())
print(a << 1)


# 6047. [기초-비트시프트연산] - 2의 거듭제곱 배로 곱해 출력하기
a, b = input().split()
a, b = int(a), int(b)
print(a << b)

# 6048. [기초-비교연산] - 정수 2개 입력받아 비교하기1
a, b = input().split()
a, b = int(a), int(b)
print(a<b)

# 6049. [기초-비교연산] - 정수 2개 입력받아 비교하기2
a, b = input().split()
a, b = int(a), int(b)
print(a == b)

# 6050. [기초-비교연산] - 정수 2개 입력받아 비교하기3
a, b = input().split()
a, b = int(a), int(b)
print(a<=b)

# 6051. [기초-비교연산] - 정수 2개 입력받아 비교하기4
a, b = input().split()
a, b = int(a), int(b)
print(a != b)

# 6052. [기초-논리연산] - 정수 입력받아 참 거짓 평가하기
n = int(input())
print(bool(n))

# 6053. [기초-논리연산] - 참 거짓 바꾸기
a = bool(int(input()))
print(not a)

# 6054. [기초-논리연산] - 둘 다 참일 경우만 참 출력하기
a, b = input().split()
print(bool(int(a)) and bool((int(b)))) # and는 참, 참이면 참이다. 나머지는 전부 거짓

# 6055. [기초-논리연산] - 하나라도 참이면 참 출력하기
a, b = input().split()
print(bool(int(a)) or bool(int(b))) # or는 하나라도 참이면 참이고 나머지는 거짓

# 6056. [기초-논리연산] - 참/거짓이 서로 다를 때에만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# 6057. [기초-논리연산] - 참/거짓이 서로 같을 때에만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or ((not c) and (not d)))

# 6058. [기초-논리연산] - 둘 다 거짓일 경우만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not(c or d))


