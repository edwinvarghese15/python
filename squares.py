def display_squares(n):
    for i in range(1, n + 1):
        print(f"The square of {i} is {i**2}")


n = int(input("Enter a number: "))

display_squares(n)
