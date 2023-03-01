# https://www.codewars.com/kata/5511b2f550906349a70004e1/python
# 5yu
def last_digit(n1, n2):
	if(n2==0):
		return 1
	last = []
    for i in range(1,10):
    	if(str((n1**i))[-1] in last):
    		break
    	else:
    		last.append(str((n1**i))[-1])
    if(n2%len(last) != 0):
    	return int(last[(n2 % len(last)) -1])
    else:
    	return int(last[len(last)-1])


print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651))
#print(last_digit(4, 2))
#print(last_digit(9, 7))