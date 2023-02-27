# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
# 7 kyu
def find_short(s):
    l = len(s.split()[0])
    for word in s.split():
        if len(word) < l:
            l = len(word)
    return l