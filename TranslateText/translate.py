def translate(text:str)-> str:
    newText =""
    vowels = ('a','e','o', 'i','u', ' ')

    for i in text:
        if i not in vowels:
            newText += i + 'o' + i
        else:
            newText+=i

    return newText



