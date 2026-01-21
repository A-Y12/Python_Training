Student = {
    'name':'Ayush',
    'age':22,
    "city": "Kochi"
}
print (Student['name'])
print (Student['age'])
print(Student.get("email"))
print(Student.get("name"))

Student["email"] = "aa@bbb"
print (Student["email"])
Student["city"] = "Kolkata"
print (Student.get("city"))

#print
for k in Student.keys():
    print(k)
for v in Student.values():
    print(v)
for k,v in Student.items():
    print(k,v)
print(Student)


#remove
Student.pop("age") #remove by key
print (Student)
del Student["city"]  #delete
print (Student)
Student.clear() #empty dictionary
print (Student)