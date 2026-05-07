#remove all the vowel from the string
def remove_vowel():
    word=input("enter a string: ")
    vowel="aeiouAEIOU"
    new_string=""
    for i in word:
        if i not in vowel:
            new_string=new_string + i
        
    print("string without vowels",new_string)
remove_vowel()
