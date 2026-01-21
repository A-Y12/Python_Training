l=[1,2,3,3,4,5,6]
def access(i):
    try:
        print(l[i])
    except IndexError as e:
        print("Index out of range")

access(8)