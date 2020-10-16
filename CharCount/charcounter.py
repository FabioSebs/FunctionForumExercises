def char_freq(word:str):
    #this appends the count of every char in the string
    #problem is that there are duplicates
    char_count = [str(word.count(i)) for i in word]
    char_list = [i for i in word]

    return dict(zip(char_list, char_count))
    
    
    
