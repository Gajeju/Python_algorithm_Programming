# 8퀸 문제 알고리즘 구현하기

pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 16
flag_c = [False] * 16

def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if (    not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)