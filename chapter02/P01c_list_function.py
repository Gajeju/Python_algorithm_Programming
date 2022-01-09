# 언팩

x = [1, 2, 3]
a, b, c = x
print(a, b, c)

# 인덱스 접근

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

# len()

x = [15, 64, 7, 3.14, [21,55], 'ABC']
print(len(x))

# 빈 배열 판단

x = []
if x:
    print("not empty")
else:
    print("empty")

# 배열의 대소 비교

print([1,2,3] == [1,2,3])
print([1,2,3] < [1,2,4])
print([1,2,3,4] <= [1,2,3,4])
print([1,2,3] < [1,2,3,4,5])
print([1,2,3] < [1,2,3,5] < [1,2,3,5,6])
print([1,2,4] < [1,2,3,4,5])

# 내포

numbers = [1,2,3,4,5]
twise = [num * 2 for num in numbers if num % 2 == 1]
print(twise)
