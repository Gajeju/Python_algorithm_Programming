# 버블 정렬 알고리즘 구현하기 (정렬 과정을 출력)

from typing import MutableSequence

def bubble_sort_verbos(a: MutableSequence) -> None:
    """버블 정렬(정렬 과정을 출력)"""
    ccnt = 0    # 비교 횟수
    scnt = 0    # 교환 횟수
    
    n = len(a)
    for i in range(n - 1):
        print(f'패스 {i+1}')
        exchange = 0
        for j in range(n-1, i, -1):
            for m in range(0, n-1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                     ' +' if a[j - 1] > a[j] else ' -'),
                                     end='')
            print(f'{a[n-1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange += 1
        for m in range(0, n-1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n-1]:2}')
        if exchange == 0:
            break
    print(f'비고를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')


if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    bubble_sort_verbos(x)
    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')