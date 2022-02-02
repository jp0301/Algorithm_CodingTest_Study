
n, m = map(int, input().strip().split(' '))

for i in  range(m):
    for j in range(n):
        print('*', end='') 
    print()


"""
Other solution 연산자 사용
n, m = map(int, input().strip().split(' '))
answer = ('*' * a + '\n') * b
print(answer)

"""
