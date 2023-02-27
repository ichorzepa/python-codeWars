# https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# 6 kyu
def find_nb(m):
	used=0
	count = 0
	while used < m:
		used = used + (count+1)**3
		count += 1
	return -1 if used!=m else count

print(find_nb(1071225))
#print(find_nb(4183059834009))
#print(find_nb(24723578342962))