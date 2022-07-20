print("Welcome to my Computer quiz!")
playing = input("Do you want to play? yes (or) no ")
if playing.lower() != "yes":
    quit()
print("Okay let's play")
score = 0
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does DRAM stand for? ")
if answer.lower() == "dynamic random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
if score == 0:
    print("you are stupid")
elif score == 3:
    print("your are genius")
print("You got " + str(score) + " questions correct")
print("You got " + str((score / 3) * 100) + "%")
