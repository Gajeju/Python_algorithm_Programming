# 리스트의 모든 원소를 역순으로 스캔하기

x = ['John', 'George', 'Paul', 'Ringo']

x = x[::-1]
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')

x.reverse()
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')

x = list(reversed(x))
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
