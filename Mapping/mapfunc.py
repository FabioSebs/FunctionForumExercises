def wordcount(lst:[str]):
    lst2 = []
    
    for i in range(len(lst)):
        lst2.append(len(lst[i]))

    final_lst = dict(zip(lst, lst2))

    print(final_lst)
