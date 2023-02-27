def longest(a1, a2):
    text = a1 + a2
    unique = set(text)
    return "".join(sorted(unique))


print(longest("aretheyhere", "yestheyarehere"))