# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
# 5kyu
import string
def rot13(message):
    alphabet = string.ascii_letters
    mess_encrypted = []
    for ch in list(message):
        if ch in alphabet:
            if(ord(ch) > 109):
                mess_encrypted.append(chr(ord(ch)-13))
            elif(ord(ch) <= 109 and ord(ch)>=97):
                mess_encrypted.append(chr(ord(ch)+13))
            elif(ord(ch) <= 90 and ord(ch)>77):
                mess_encrypted.append(chr(ord(ch)-13))
            elif(ord(ch) <=77 and ord(ch)>=65):
                mess_encrypted.append(chr(ord(ch)+13))
        else:
            mess_encrypted.append(ch)
    return "".join(mess_encrypted)

print(rot13('test'))
print(rot13('Test'))
print(rot13('aA bB zZ 1234 *!?%'))