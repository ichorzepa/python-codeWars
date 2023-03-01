# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/python
# 5kyu
def zeros(n):
	count=0
	while n>=5:
		n//=5
		count += n
	return count


print(zeros(30))