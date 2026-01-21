with open("Ayush.txt", "w") as f:
    try:
        str = input("Enter a string")
    except ValueError:
        print("Please enter a string")
    except FileNotFoundError:
        print("File not found")
    else:
        f.write(str)

        