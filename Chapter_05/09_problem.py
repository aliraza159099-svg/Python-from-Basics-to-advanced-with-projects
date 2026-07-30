# Check its length
s = set()
s.add(10)
s.add(10.00)
s.add('10')
print(len(s)) # Here 10 == 10.00 so length is 2

q = {} #Is it a set or dictionary?
print(type(q))
