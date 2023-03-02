# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
# 5kyu

def domain_name(url):
	if(url[0:5] == "http:"):
		if(url[7:10] == "www"):
			return url[11:].split(".")[0]
		else:
			return url[7:].split(".")[0]
	elif(url[0:5] == "https"):
		if(url[8:11] == "www"):
			return url[12:].split(".")[0]
		else:
			return url[8:].split(".")[0]
	elif(url[0:3] == "www"):
		return url[4:].split(".")[0]
	return url

print(domain_name("www.xakep.ru"))
#print(domain_name("http://www.xakep.ru"))
#print(domain_name("https://google.com"))
#print(domain_name("https://www.google.com"))