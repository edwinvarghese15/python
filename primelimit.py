def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_prime(n):
    count = 0
    num = 2
    primes = []
   
    while count < n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    
    return primes


a = int(input("Enter the limit: "))
prime_numbers = print_prime(a)  
print(prime_numbers)  

