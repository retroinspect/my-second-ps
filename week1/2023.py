
n_digit_prime = [[2, 3, 5, 7]]
prime_last_digit = [1, 3, 7, 9]

def isPrime(num):
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


N = int(input())
for i in range(1, N):
    i_digit_prime = []
    
    for seed in n_digit_prime[i-1]:
        for last_digit in prime_last_digit:
            num = seed * 10 + last_digit
            if (isPrime(num)):
                i_digit_prime.append(num)
    
    n_digit_prime.append(i_digit_prime)

for prime in n_digit_prime[N-1]:
    print(prime)