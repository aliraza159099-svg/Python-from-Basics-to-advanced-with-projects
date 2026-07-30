

def table():
    for i in range(1,11):
        with open(f"table/table{i}.txt",mode="w") as f:
            for j in range(1,21):
                f.write(f"{i} x {j} = {i*j}\n")

table()