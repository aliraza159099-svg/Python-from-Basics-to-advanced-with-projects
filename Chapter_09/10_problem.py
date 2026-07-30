
with open("pro10.txt") as f:
    content = f.read()

newContent = content.replace("Animals","#######")

with open("pro10.txt","a") as f:
    content = f.write(newContent)