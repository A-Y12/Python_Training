try:
    with open("students.txt","r") as f:
        f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
    