def overlapping(lst1:list,lst2:list)->bool:
    
    for i in lst1:
        for x in range(len(lst2)):
            if i == lst2[x]:
                return True
    return False