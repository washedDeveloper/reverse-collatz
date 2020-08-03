import random

print("\nReverse Collatz")
print("---------------")
print("This is a puzzle game where you need to find a path")
print("You start a 1 and need to traverse to another number using only two operation")
print("The first operation is to multiply by 2 or you can subtract 1 and divide by three.")

play_option = input("Would you like to play? (y or n) ")


def calculate_steps(target):
    steps = 0
    if target <= 1:
        return steps
    while target != 1:
        if target % 2 == 0:
            target /= 2
            steps += 1
        else:
            target = (target * 3) + 1
            steps += 1
    return steps


def game_loop():
    target = random.randint(2, 100)
    current = 1
    steps_to_target = calculate_steps(target)
    total_steps_taken = 0
    for i in range(steps_to_target):
        print(f"\nCurrent: {current}")
        print(f"Steps Taken: {total_steps_taken}")
        print(f"Target: {target}")
        print(f"Steps Left: {steps_to_target - total_steps_taken}\n")
        choice = int(
            input("1. Multiply by 2\n2. Subtract 1 and Divide by 3\n"))

        if(choice == 1):
            current *= 2
            total_steps_taken += 1
        elif(choice == 2):
            current = (current // 3) + 1
            total_steps_taken += 1
    if current == target and total_steps_taken == steps_to_target:
        print("You Won!")
        print("Press enter to quit.")
        input()
    else:
        print("You Lost!")
        print("Press enter to quit.")
        input()


if(play_option == "y"):
    game_loop()
else:
    exit()
