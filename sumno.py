def sum_numbers(n):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i
    return sum1

n = int(input("Enter the number\n"))
result = sum_numbers(n)
print(f"The sum of numbers from 1 to {n} is {result}")

