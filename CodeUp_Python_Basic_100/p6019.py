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
