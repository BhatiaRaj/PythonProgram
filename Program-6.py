# Write a program by asking the user for a string and print out whether this string is a palindrome or not. (Apalindrome is a string that reads the same forwards and backwards.)

def isPalindrome(s):
    return s == s[::-1]


s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")
