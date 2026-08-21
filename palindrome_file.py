i = input('Enter a word : ')

if i == i[::-1]:
    print(i[::-1],'is a palindrome')
else:
    print(i,'is not a palindrome')