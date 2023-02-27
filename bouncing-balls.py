def bouncing_ball(h, bounce, window):
    sum=1

    if (h<=0):
        return -1
    elif (bounce <=0 or bounce >= 1):
        return -1
    elif (window >= h):
        return -1

    while h > window:
        print(h)
        h = h * bounce
        if (h > window):
            sum = sum + 2
    return sum

#print(bouncing_ball(2, 0.5, 1))
#print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))