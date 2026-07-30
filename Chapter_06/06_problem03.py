p1 = "Make money with me"
p2 = "easy way to earn"
p3 = "just send your details"

comment = input("Enter your comment: ")
if p1 in comment or p2 in comment or p3 in comment:
    print("Moved to spam")
else:
    print("Moved to inbox")
