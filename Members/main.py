import members as m

if __name__ == "__main__":
    print(m.is_member(1, [2,3,4,1]))
    print(m.is_member('a', [5,8,4,'a']))
    print(m.is_member(1, [2,3,4,0]))
