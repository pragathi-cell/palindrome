
# Program to check whether a string is a palindrome
import sys

string = sys.argv[1]

# Reverse the string
reverse = string[::-1]

# Check palindrome
if string == reverse:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
    print("usn:01fe25bca151")
