# Python3 program to find sum of
# series of 1 + x^2 + x^3 + ....+ x^n

# Function to find the sum of
# the series and print N terms
# of the given series
def sum(x, n):
	
	total = 1.0
	multi = x

	# First Term
	print(1, end = " ")

	# Loop to print the N terms
	# of the series and find their sum
	for i in range(1, n):
		
		total = total + multi
		print('%.1f' % multi, end = " ")
		multi = multi * x
		
	print('\n')
	return total;

# Driver code
x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
print('%.2f' % sum(x, n))

# This code is contributed by Pratik Basu
