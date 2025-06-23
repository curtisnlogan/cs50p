# dicts can be nested within a list, which can be accessed seperately
# using subscripts
students_ld = [
    {
        'name': 'hermoine',
        'house': 'gryffindor',
        'patronus': 'otter',
    },
    {
        'name': 'harry',
        'house': 'gryffindor',
        'patronus': 'stag',
    },
    {
        'name': 'ron',
        'house': 'gryffindor',
        'patronus': 'jack russel terrier',
    },
    {
        'name': 'draco',
        'house': 'slytherin',
        'patronus': None,  # None represents the absence of a value 
        # and makes it clear
    }
]

for i, (name, house, patronus) in enumerate(students_ld, start=1):
    print(i, house)


students = ["hermione", "harry", "ron"]

students_d = {  # best to put each key and value on a new line for readability
    "hermoine": "Gryffindor",
    "harry": "Gryffindor",
    "ron": "Gryffindor",
    "Draco": "Slytherin",
}

# 'enumerate' good for when one needs both a number and the index
for i, (student, house) in enumerate(students_d.items(), start=1):
    print(f"{i} Student: {student} House: {house}")
print(students_d["Draco"])

houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


# get use to counting from 0 up and not 1
print(students[0])


for student in students[0:2]:  # an example of subscripting in a for loop
    print(student)

for i in range(len(students)):  # 'len' purpose in life to tell how long a
    # list is
    print(i + 1, students[i])  # 'print' can take two arguments
