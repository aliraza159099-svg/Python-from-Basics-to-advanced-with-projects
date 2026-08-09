
dic = {
    "Ali":12,
    "Ahmed":16,
    "Sahil":17,
    "Bari":19,
    "Adil": 21
}

def addStudent(name,roll_no):
    dic.update({name:roll_no})
    print("Student added successfully")
    with open("student.txt","w") as f:
        f.write(str(dic))

def remStudent(name):
    if name in dic:
         dic.pop(name)
         print("Student removed successfully")
         with open("student.txt","w") as f:
             f.write(str(dic))
    else:
        print("Student is ")

def searchStudent(name):
        with open("student.txt") as f:
            student = f.read()
        if name in student:
            print("Student found")
        else:
            print("Not found.")
num=1
while num != 5:
    print("1.Add student \n2.Remove Student \n3.See the students \n4. Search Student \n5. Exit ")
    num = int(input("........Enter your choice........\n"))
    if num == 1:
        name = input("Enter student's name: ")
        roll = int(input("Enter roll no: "))
        addStudent(name,roll)
    elif num == 2:
        name = input("Enter student's name: ")
        remStudent(name)
    elif num == 3:
        print(dic)
    elif num == 4:
        name = input("Enter name of the student: ")
        searchStudent(name)
    elif num == 5:
        print("Thanks")