def makeForming(verb:str):
    
    if verb.endswith('ie') or verb.endswith('e'):
        temp = verb[-2:]
        temp2 = verb[-1]
        temp = temp.replace("ie", "ying")
        temp2 = temp2.replace("e", "ing")
        
        return verb[:-1]+temp2 if len(temp2)>1 and len(temp)!=4 else verb[:-2]+temp
        

    return {
        'a':verb+verb[-1]+"ing",
        'e':verb+verb[-1]+"ing",
        'i':verb+verb[-1]+"ing",
        'o':verb+verb[-1]+"ing",
        'u':verb+verb[-1]+"ing",

    }.get(verb[-2], verb+"ing")
