# 6032. [기초-산술연산] - 정수 1개 입력받아 부호 바꾸기
a = input()
n = int(a)
print(-n)

# 6033. [기초-산술연산] - 문자 1개 입력받아 다음 문자 출력하기
c = ord(input())
print(chr(c+1))
# ord() 함수는 특정한 값을 아스키 코드로 변환해주는 함수
# chr() 함수는 아스키 코드 값을 ->>> 문자로 변환 

# 6034. [기초-산술연산] - 정수 2개 입력받아 차 계산하기
a, b = input().split()
c = int(a) - int(b)
print(c)

# 6035. [기초-산술연산] - 실수 2개 입력받아 곱 계산하기
f1, f2 = input().split()
m = float(a) - float(b)
print(m)

# 6036. [기초-산술연산] - 단어 여러 번 출력하기
w, n = input().split()
print(w * int(n))

# 6037. [기초-산술연산] - 문장 여러 번 출력하기
n = input()
s = input()
print(int(n)*s)

# 6038. [기초-산술연산] - 정수 2개 입력받아 거듭제곱 계산하기
a, b = input().split()
c = int(a) ** int(b)
print(c)

# 6039. [기초-산술연산] - 실수 2개 입력받아 거듭제곱 계산하기
a, b = input().split()
c = float(a) ** float(b)
print(c)

# 6040. [기초-산술연산] - 정수 2개 입력받아 나눈 몫 계산하기
a, b = input().split()
print(a//b)

