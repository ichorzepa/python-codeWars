# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
# 6kyu 
def spin_words(sentence):
    spinned = []
    for word in sentence.split():
        if(len(word) >= 5):
            spinned.append(word[::-1])
        else:
            spinned.append(word)
    return " ".join(spinned)


print(spin_words("Hey fellow warriors"))