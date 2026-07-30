students = {}
def add_student(name,roll_no):
    students.update({name:roll_no})

num=1
while num!=0:
    name = input("Enter name : ")
    roll_no = int(input("Enter roll no : "))
    add_student(name,roll_no)
    num = int(input("Enter 0 exits "))

print(students)