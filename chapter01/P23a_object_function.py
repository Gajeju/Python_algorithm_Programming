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