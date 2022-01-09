# 드모르간 법칙 사용

print("2자리 양수를 입력하세요.")

while True:
    no = int(input("값을 입력하세요.: "))
    if not(no < 10 or no > 99):
        break
print(f"입력받은 양수는 {no}입니다.")
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