# 최댓값
'''
print('세 정수의 초댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}입니다.')
'''

# input()
'''
print('이름을 입력하세요.: ', end='')
name = input()
print(f'안녕하세요? {name} 님.')

name = input("이름을 입력하세요.: ")
print(f'안녕하세요? {name} 님.')
'''

# 형변환
print(int('17'))
print(int('0b110', 2))
print(int('0o75', 8))
print(int('13', 10))
print(int('0x3F', 16))
print(float('3.14'))


# 최대값 검증

def max(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3, 2, 1) = {max(3, 2, 1)}')    # a > b > c
print(f'max3(3, 2, 2) = {max(3, 2, 2)}')    # a > b = c
print(f'max3(3, 1, 2) = {max(3, 1, 2)}')    # a > c > b
print(f'max3(3, 2, 3) = {max(3, 2, 3)}')    # a = c > b
print(f'max3(2, 1, 3) = {max(2, 1, 3)}')    # c > a > b
print(f'max3(3, 3, 2) = {max(3, 3, 2)}')    # a = b > c
print(f'max3(3, 3, 3) = {max(3, 3, 3)}')    # a = b = c
print(f'max3(2, 2, 3) = {max(2, 2, 3)}')    # c > a = b
print(f'max3(2, 3, 1) = {max(2, 3, 1)}')    # b > a > c
print(f'max3(2, 3, 2) = {max(2, 3, 2)}')    # b > a = c
print(f'max3(1, 3, 2) = {max(1, 3, 2)}')    # b > c > a
print(f'max3(2, 3, 3) = {max(2, 3, 3)}')    # b = c > a
print(f'max3(1, 2, 3) = {max(1, 2, 3)}')    # c > b > a

# 중앙값
'''
def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')
'''

def med3(a, b, c):
    if (b >= a and c  <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

# 조건과 분김
'''
n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')
'''
'''
n = int(input('정수를 입력하세요.:'))

if n == 1:
    print('A')
elif n == 2:
    print('B')
else:
    print('C')
'''
'''
n = int(input('정수를 입력하세요.: '))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')

n = int(input('정수를 입력하세요.'))

if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
else:
    pass
'''

# 반복
'''
print ('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
'''
'''
print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = 0
for i in range(1, n+1):
    sum += i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
'''
'''
print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))

sum = n * (n + 1) // 2

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
'''
'''
# 연속하는 정수으 합 구하기
print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')
'''

