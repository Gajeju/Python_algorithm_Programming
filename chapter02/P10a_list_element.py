# 자료형을 정하지 않은 리스트 확인하기

x = [15, 64, 7, 3.14, [32, 55], 'ABC']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

x = [[1,2,3], [4,5,6]]
y = x.copy()
x[0][1] = 9
print(x,y, sep='\n')

import copy
x = [[1,2,3], [4,5,6]]
y = copy.deepcopy(x)
x[0][1] = 9
print(x,y, sep='\n')
