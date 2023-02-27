def solution(text, ending):
	return True if text[-len(ending):] == ending else False


print(solution('abc', ''))
print(solution('abc', 'bc'))
print(solution('abc', 'bccc'))
print(solution('abcddd', 'dd'))