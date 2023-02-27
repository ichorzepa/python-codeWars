def find_short(s):
    l = len(s.split()[0])
    for word in s.split():
        if len(word) < l:
            l = len(word)
    return l