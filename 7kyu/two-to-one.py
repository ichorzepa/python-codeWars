# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
# 7 kyu
def longest(a1, a2):
    text = a1 + a2
    unique = set(text)
    return "".join(sorted(unique))


print(longest("aretheyhere", "yestheyarehere"))