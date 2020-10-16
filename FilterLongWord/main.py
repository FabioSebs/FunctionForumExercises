import filterLongWord as flw

if __name__ == "__main__":
    print(flw.filter_long_words(["This" , "is" , "a", "test", "for", "function"], 2))
    print(flw.filter_long_words(["This" , "is" , "a", "test", "for", "function"], 3))
    print(flw.filter_long_words(["This" , "is" , "a", "test", "for", "function"], 4))