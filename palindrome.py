def palindrome(s):
	s_rev = s[::-1]
	return s_rev == s
while True:
	s = input("Enter the number\ enter 'exit' to exit\n")
	if s == 'exit':
		print("Exiting")
		break
		
	if palindrome(s):
		print(f"This is {s}is palindrome")
	else:
		print(f"The is  {s}is not palindrome")	
	
