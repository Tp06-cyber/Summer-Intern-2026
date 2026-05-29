import random
l=["rock","paper","scissor"]
while True:
    user=input("Enter your choice: ")
    if user not in l:
        print("Invalid input. Please try again.")
        continue
    comp=random.choice(l)
    print(f"Computer chose: {comp}")
    if user==comp:
        print("It's a tie!")
    elif (user=="rock" and comp=="scissor") or (user=="paper" and comp=="rock") or (user=="scissor" and comp=="paper"):
        print("You win!")
    else:
        print("Computer wins!") 