# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# 6 kyu
def likes(names):
	if len(names) == 0:
		display = "no one likes this"
		return display
	if len(names) == 1:
		display = names[0] + " likes this"
		return display
	if len(names) == 2:
		display = names[0] + " and " + names[1] + " like this"
		return display
	if len(names) == 3:
		display = names[0] + ", " + names[1] + " and " + names[2] + " like this"
		return display
	if len(names) > 3:
		display = names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this"
		return display
	pass



names = []
names.append("Peter")
names.append("Cam")
print(likes(names))