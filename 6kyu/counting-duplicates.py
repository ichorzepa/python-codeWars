# https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# 6 kyu
import string
def duplicate_count(text):
	count = 0
	for c in string.ascii_lowercase:
		if (text.lower().count(c) > 1):
			count +=1
	for n in string.digits:
		if (text.count(n) > 1):
			count +=1
	return count


print(duplicate_count("ZiSkqTSq8SKgCmvG0ndfcTTRUrQ9GoQyEhEdYLuqkfB1WdzaYMD5Nvn36Id9JuHPEdlqqlFFpoDBaQEUOMWwxsncGlSi"))