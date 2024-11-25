def display_vowels(word):
    vowels = "aeiouAEIOU"  
    found_vowels = []  
   
    for char in word:
        if char in vowels:
            found_vowels.append(char)
    
    if found_vowels:
        print("Vowels in the word:", ", ".join(found_vowels))
    else:
        print("No vowels found in the word.")

word = input("Enter a word: ")
display_vowels(word)

