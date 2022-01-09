# 반복문 건너뛰기와 여러 범위 스캔하기
# 1~12까지 8을 건너뛰고 출력하기

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()


for i in list(range(1,8)) + list(range(9,13)):
    print(i, end='')
print()