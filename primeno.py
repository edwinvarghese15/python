def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i ** 0.5) + 1): 
                if i % j == 0:
                    break
            else:  
                prime_list.append(i)
    return prime_list

n = int(input("Enter the starting range: "))
m = int(input("Enter the ending range: "))
lst = prime(n, m)

if len(lst) == 0:
    print("No prime no in this range")
else:
    print(lst)

