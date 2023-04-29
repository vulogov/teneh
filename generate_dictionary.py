c = ["b" , "p" , "v" , "f" , "g" , "k" , "d" , "t" , "z" , "s" , "ž" , "š" , "m" , "l" , "n" ]
v = ["a" , "o" , "i" , "u" , "e" , "ā" , "ō" , "ī" , "ū" , "ē"]

for c1 in c:
    for v1 in v:
        for c2 in c:
            print("%s%s%s"%(c1,v1,c2))
