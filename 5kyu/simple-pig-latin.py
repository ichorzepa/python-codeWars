# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
# 5kyu

def pig_it(text):
	result = []
	for words in text.split(" "):
		if words.isalpha():
			result.append(words[1:] + words[0] + "ay")
		else:
			result.append(words)
	return " ".join(result)


print(pig_it('Pig latin is cool'))
print(pig_it('Quis custodiet ipsos custodes ?'))