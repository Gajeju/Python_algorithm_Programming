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
