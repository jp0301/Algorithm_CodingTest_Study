# 6019. [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.')
print(y, m, d, sep=('-'))

# 6020. [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
f, b = input().split('-')
print(f, b, sep=(''))

# 6021. [기초-입출력] 단어 1개 입력받아 나누어 출력하기
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022. [기초-입출력] 연월일 입력받아 나누어 출력하기
s = input()
print(s[0:2], s[2:4], s[4:6])

# 6023. [기초-입출력] 시분초 입력받아 분만 출력하기
h, m, s = input().split(':')
print(m)

# 6024. [기초-입출력] 단어 2개 입력받아 이어 붙이기
w1, w2 = input().split()
s = w1 + w2
print(s)

# 6025. [기초-값변환] 정수 2개 입력받아 합 게산하기
a, b = input().split()
n = int(a) + int(b)
print(n)

# 6026. [기초-값변환] 실수 2개 입력받아 합 계산하기
a = input()
b = input()

f = float(a) + float(b)
print(f)

# 6027. [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1
a = input()
n = int(a)
print('%x'%n)

# 6028. [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2
a = input()
n = int(a)
print('%X'%n)

# 6029. [기초-값변환] 16진수 정수 입력받아 8진수로 출력하기
w1, w2 = input().split()
s = w1 + w2
print(s)

# 6030. [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기
a = input()
n = int(a, 16)
print('%o'%n)

# 6031. [기초-값변환] 정수 1개 입력받아 유니코드 문자로 변환하기
n = ord(input())
print(n)
