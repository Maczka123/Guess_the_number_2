# Function which is asking user if selected by computer number
# is too big, too small or you win.
def user_answer():
    inputs = ["you win", "too big", "too small"]
    while True:
        user_input = input("Is number 'too big', 'too small' or 'you win: ").lower()
        if user_input in inputs:
            break
        else:
            print("Your answer is wrong.")
    return user_input


# Main function which is trying to hit number selected by user.
def guess_the_number():
    print("Choose the number from 0 to 1000.")
    print("Press 'Enter'' to start")
    input()
    min = 0
    max = 1000
    user_choice = ""
    while user_choice != "you win":
        guess = int(((max-min)//2) + min)
        print(f"I will guess : {guess}")
        user_choice = user_answer()
        if user_choice == "too big":
            max = guess
        elif user_choice == "too small":
            min = guess
    print("I won!!!")

guess_the_number()