# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
# 6 kyu
def is_valid_walk(walk):
    if(len(walk) != 10):
    	return False
    else:
    	move = [0,0]
    	for movements in walk:
    		if(movements == "e"):
    			move[0] -= 1
    		elif (movements == "w"):
    			move[0] += 1
    		elif (movements == "n"):
    			move[1] -= 1
    		elif (movements == "s"):
    			move[1] += 1
    	if(move == [0,0]):
    		return True
    	else:
    		return False

#print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
#print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))