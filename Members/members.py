def is_member(x , y:list):
    while len(y)!=0:
        if x == y[0]:
            return True

        else:   
            y.pop(0)
    return False


