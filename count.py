string=input("Enter a string:")
alphabet=input("Enter a alphabet")
count=0
for char in string:
		if char==alphabet:
			count+=1
print("The number of 'alphabet' occurence in the string is:",count)
