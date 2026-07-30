#if elif else ladder

print("................Votoers age Valdator.................")
age = int(input("Enter your age: "))

if(age>=150):
  print("Unrealistic age.")
elif(age>=18):
  print("You are eligible for voting in Pakistan.")
else:
  print(f"You are not eligible for voting you can vote after {18-age} years.")


print("......:End of program:....... ")
