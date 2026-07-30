'''
Checking whether a student is paased or failed the test 
pass eligibility: 33% in each and 50% overall percentage
enetered by the user
'''
print("..........Enter numbers out of 100..........")
sub1 = int(input("Enter thr mark of subject1: "))
sub2 = int(input("Enter thr mark of subject2: "))
sub3 = int(input("Enter thr mark of subject3: "))
total = (((sub1+sub2+sub3)/300)*100)

if total >= 50 and (sub1 >= 33 and sub2 >= 33 and sub3 >= 33): #can be write without ()
    print("you are passed")
else:
    print("You are failed")