# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
# 7 kyu
def solution(text, ending):
	return True if text[-len(ending):] == ending else False


print(solution('abc', ''))
print(solution('abc', 'bc'))
print(solution('abc', 'bccc'))
print(solution('abcddd', 'dd'))