# palindrome

i = input('enter a word: ')

if i == i[::-1]:
    print('is a palindrome')
else:
    print('is not a palindrome')