c = ["b" , "p" , "v" , "f" , "g" , "k" , "d" , "t" , "z" , "s" , "ž" , "š" , "m" , "l" , "n" ]
v = ["a" , "o" , "i" , "u" , "e" , "ā" , "ō" , "ī" , "ū" , "ē"]

def gen_root():
    for c1 in c:
        for v1 in v:
            for c2 in c:
                yield "%s%s%s"%(c1,v1,c2)

for r1 in gen_root():
    print(r1)
    for r2 in gen_root():
        print("%s%s"%(r1,r2))
