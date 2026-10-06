import json
file=open("student.json",'r')
data = json.load(file)

file.close()
print(data)
print(" ")

students = data["students"]
for student in students:
    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Marks:", student["marks"])
    print()