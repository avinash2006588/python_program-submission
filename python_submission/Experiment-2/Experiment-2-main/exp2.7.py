def palindrome(word):
    if word == word[::-1]:
        return True
    return False


word = input("Enter a word: ")

if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")
