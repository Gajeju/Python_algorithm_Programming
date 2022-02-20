# 정렬을 마친 두 배열 병합하기

from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)

    while pa < na and pb < nb:
        if a[pa] < b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:
        c[pc] = a[pa]
        pa +=1
        pc += 1

    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1

if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('정렬을 마친 두 배열의 병합을 수행합니다.')

    merge_sorted_list(a, b, c)

    print('배열 a와 b를 병합하여 배열 c에 저장했습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')