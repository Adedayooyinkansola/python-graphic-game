score = 0

def quiz1():
    global score
    print("quiz")
    choice1 = input("Is london in the UK? 1. Yes, 2. No")
    if (choice1 == "1"):
        print("correct")
        score += 1
        print(score)
    else:
        print("wrong")

print("Welcome to Oyinkansola's Quiz")
while True:
    choice = input("Enter choice: 1. Quiz, 2. Quit")
    if choice == "1":
        quiz1()
    else:
        break