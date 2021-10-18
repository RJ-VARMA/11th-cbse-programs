# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = str(input("Enter the String...:"))
s=s.lower()
print(s)
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
