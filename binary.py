binary = input("Enter the Binary variables\n")
decimal=0
for i in binary:
	decimal=decimal * 2 + int(i)
print(f"The binary value of{binary} is {decimal}")	
