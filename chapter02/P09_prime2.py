# 소수 나열 알고리즘 개선 1
# 2부터 n-1까지 어떤 소수로도 나누어지지 않으면 소수

counter = 0     # 나눗셈 횟수
ptr = 0         # 찾은 소수의 개수 (다음에 저장할 인덱스)
prime = [None] * 500

prime[ptr] = 2  # 초기값 2등록
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1
    
for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')
