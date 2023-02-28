# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# 6kyu
def digital_root(n):
	while (len(str(n))>1):
		x = list(str(n))
		n=0
		for i in range(0,len(x)):
			n = n + int(x[i])
	return n


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))