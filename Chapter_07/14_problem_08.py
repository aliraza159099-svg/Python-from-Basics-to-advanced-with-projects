# From a list print those name with A as srarting alphabet

l = ["Raza","Ahmed","Akbar","Kabir","Bari","HAssaon","Adil"]

for name in l:
    if(name.startswith("A") or name.endswith("a")):
        print(f"Hello, {name}")