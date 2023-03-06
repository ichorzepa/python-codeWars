# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
# 7 kyu
def printer_error(s):
	count=0
	for character in s:
		if ord(character) in range(110, 123):
			count += 1
	return str(count) + "/" + str(len(s))



print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"))
#print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))