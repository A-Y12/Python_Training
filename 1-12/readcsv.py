import csv
try:
    with open("students.csv","r") as f:
        reader = csv.reader(f)
except csv.Error as e:
    print("The file is not formatted correctly")

