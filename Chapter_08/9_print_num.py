
#Print from N to 1
def num(n):
    if n == 1:
        print("1")
        return 1
    print(n)
    return num(n-1)

num(5)

#Printing from 1 to N

def num_one_to_N(n):
    if n == 1:
        print("1")
        return 1
    return n-1



num_one_to_N(5)
