# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/python
# 5 kyu

def scramble(s1, s2):
	u1 = list(set(s1))
	u2 = list(set(s2))
	for character in u2:
		if u1.count(character) < u2.count(character):
			return False
	return True
		

print(scramble('rkqodlwww', 'world'))
print(scramble('katas', 'steak'))