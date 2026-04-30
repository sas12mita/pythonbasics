#string is a palindrome or not
def palindorme():
    string=input("Enter a string")
    rev_string=string[::-1]
    if string.lower==rev_string.lower():
        print("String is palindrome")
    else:
        print("string is not a palindrome")

#count vowels and consonents in a string
word = input("Enter a string: ")

vowels = "aeiouAEIOU"
count_vowel = 0
count_consonant = 0

for ch in word:
    if ch in vowels:
        count_vowel += 1
    elif ch != " ":   # ignore spaces
        count_consonant += 1

print("Vowels count:", count_vowel)
print("Consonants count:", count_consonant)
#count the total number of words in the sentence(without len())


def count_word(word):
    sentence=input("enter a string")
    sentence=sentence.split()
    count=0
    for i in sentence:
        count=count+1
    print("the total words in sentence",count)
    count_word()


