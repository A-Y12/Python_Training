

lists = [1,2,"a",3,4,5,6]
conv=[]
for l in lists:
    try:
        conv.append(int(l))
    except ValueError:
        print("Cant convert to int")
        conv.append(None)

print(conv)




