import random 

def game():
    score = random.randint(1,60)
    with open("score.txt","r") as f:
        highscore = f.read()
        if highscore != "":
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your score is : {score}")
    if score > highscore:
        with open("score.txt",mode="w") as q:
            q.write(str(score))

game()


