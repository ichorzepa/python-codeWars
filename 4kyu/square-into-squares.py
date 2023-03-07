def decompose(n):
	n2 = n**2
	elements = []
	sum = 0
	for num in reversed(range(1,n)):
		if(num**2 <= n2):
			n2 -= num**2
			elements.append(num)
			sum += num**2
	if sum != n**2:
		return None
	else:
		return sorted(elements)

print(decompose(50))