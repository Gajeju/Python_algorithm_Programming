# 리스트에서 임의의 원소삾을 업데이트하기
# mutable 객체의 인수 전달

def change(lst, idx, val):
    """lst[idx]의 값을 val로 업데이트"""
    lst [idx] = val

x = [11, 22, 33, 44, 55]
print('x = ', x)

index = int(input('업데이트할 인덱스를 선택하세요.: '))
value = int(input('새로운 값을 입력하세요.: '))

change(x, index, value)
print(f'x = {x}')
