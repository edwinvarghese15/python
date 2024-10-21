def power(base,exponent):
		if exponent==0:
			return 1
		else:
			return base*power(base,exponent-1)
base=float(input("Enter the value of base:"))
exponent=int(input("Enter the value of the exponent:"))
result=power(base,exponent)
print("Result is:",result)
