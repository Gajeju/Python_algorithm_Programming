# 배열 개념
'''
print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번 학생의 점수를 입력하세요.: '))
score2 = int(input('2번 학생의 점수를 입력하세요.: '))
score3 = int(input('3번 학생의 점수를 입력하세요.: '))
score4 = int(input('4번 학생의 점수를 입력하세요.: '))
score5 = int(input('5번 학생의 점수를 입력하세요.: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점입니다.')
print(f'평균은 {total / 5}점입니다.')
'''

# list
list01 = []
list02 = [1, 2, 3]
list03 = ['A', 'B', 'C']
list04 = list()
list05 = list('ABC')
list06 = list([1,2,3])
list07 = list((1,2,3))
list08 = list({1,2,3})
list09 = list(range(7))
list10 = list(range(3,8))
list11 = list(range(3, 13, 2))
list12 = [None] * 5               #원소가 5개이면서 원소값이 없는 리스트

# tuple
tuple01 = ()
tuple02 = 1,
tuple03 = (1,)
tuple04 = 1, 2, 3
tuple05 = 1, 2, 3,
tuple06 = (1, 2, 3)
tuple07 = (1, 2, 3, )
tuple08 = 'A', 'B', 'C'
tuple09 = tuple()
tuple10 = tuple('ABC')
tuple11 = tuple([1, 2, 3])
tuple12 = tuple({1, 2, 3})
tuple13 = tuple(range(7))
tuple14 = tuple(range(3, 8))
tuple15 = tuple(range(3, 13, 2))

# 언팩
x = [1, 2, 3]
a, b, c = x
print(a, b, c)

# 인덱스

x = [11, 22, 33, 44, 55, 66, 77]
print(x[2])
print(x[-3])

x[-4] = 3.14
print(x)
#print(x[7])     #error !
#x[7] = 3.14     #error !

# 슬라이스
s = [11, 22, 33, 44, 55, 66, 77]
print(s[0:6])
print(s[0:7])
print(s[0:7:2])
print(s[-4:-2])
print(s[3:1])

