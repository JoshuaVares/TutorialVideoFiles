guess = 0

while True:
    print("I’m tall when I’m young and I’m short when I’m old. What am I?")
    print("Type your guess, or type 'help1', help2', or 'I give up' below.")
    answer = input()
    guess += 1

    if "candle" in answer:
        print("You win!")
        print("It took you " + str(guess) + " guesses.")
        break

    elif answer == "help1":
        print("I give light")

    elif answer == "help2":
        print("I'm made of wax.")

    elif answer.upper() == "I GIVE UP":
        print("The answer was candle!")
        break

    else:
        print("Try again!")
