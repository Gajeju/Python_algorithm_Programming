
# 반복+조건 2
'''
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')
print()
'''
'''
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(1, n+1):
    if i % 2:
        print('+', end='')
    else:
        print('-', end='')
print()
'''
'''
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')

print()
'''

# 반복+조건 3
'''
print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요: '))
w = int(input('몇 개마다 줄바꿈할까요: '))

for i in range(n):
    print('*', end='')
    if i % w == w -1:
        print()

if n % w:
    print()
'''
'''
print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)
'''
'''
# 양수만 입력받기
print('1부터 n까지의 정수의 합을 구합니다.')

while True:
    n = int(input('n값을 입력하세요.: '))
    if n > 0:
        break
sum = 0
i = 1
for i in range(1, n+1):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
'''

# 직사각형 넓이로 변의 길이 구하기
'''
area = int(input('직사각형의 넓이를 입력하세요.:'))
for i in range(1,area+1):
    if i*i > area: break
    if area % i: continue
    print(f'{i} x {area // i}')
'''

# for_else
'''
import random

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.')
'''

# 반복문 건너뛰기와 여러 범위 스캔하기
for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()


for i in list(range(1,8)) + list(range(9,13)):
    print(i, end='')
print()

# 비교연산자 연속 사용
'''
print("2자리 양수를 입력하세요.")

while True:
    no = int(input("값을 입력하세요.: "))
    if no >= 10 and no <= 99:
        break
print(f"입력받은 양수는 {no}입니다.")

print("2자리 양수를 입력하세요.")

while True:
    no = int(input("값을 입력하세요.: "))
    if 10 <= no <= 99:
        break
print(f"입력받은 양수는 {no}입니다.")
'''
# 드모르간 법칙
'''
print("2자리 양수를 입력하세요.")

while True:
    no = int(input("값을 입력하세요.: "))
    if not(no < 10 or no > 99):
        break
print(f"입력받은 양수는 {no}입니다.")
'''

# 다중루프
print('-' * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end='')
    print()
print('-' * 27)

# 다중루프 2
'''
print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를입력하세요.: '))

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()
'''
'''
print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요.: '))

for i in range(n):
    for _ in range(n - i -1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()
'''

# 파이썬 변수의 의미
n = 1
def put_id():
    x = 1
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()

for i in range(1, 101):
    print(f'i = {i:3}   id(i) = {id(i)}')