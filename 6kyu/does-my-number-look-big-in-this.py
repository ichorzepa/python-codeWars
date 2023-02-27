# https://www.codewars.com/kata/5287e858c6b5a9678200083c
# 6 kyu
def narcissistic( value ):
	numbers = list(str(value))
	sum = 0
	for number in numbers:
		sum = sum + (int(number) ** len(numbers))
	return True if sum == value else False


print(narcissistic(371))
print(narcissistic(122))
