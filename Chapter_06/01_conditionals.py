
'''Certain conditions are check and run program if the condition met
 For syntax the condition is to write inside () and put : at the end and 
put indendation aafter the if else statement '''

print("................Votoers age Valdator.................")
age = int(input("Enter your age: "))
if(age>=18):
  print("You are eligible for voting in Pakistan.")

else:
  print(f"You are not eligible for voting you can vote after {18-age} years.")



