'''
its a problem here we are checking whether a given text is 
in the file or not using if statement
'''

with open("ali.txt") as f:
    content = f.read()
    if "Ali " in content:
        print("I am ali is in the content")
    else:
        print("I am ali is not in the text")