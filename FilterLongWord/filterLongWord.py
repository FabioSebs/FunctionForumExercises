def filter_long_words(lwords:str , n:int):
    filtered_list = [lwords[i] for i in range(len(lwords)) if len(lwords[i])>n]
    return filtered_list