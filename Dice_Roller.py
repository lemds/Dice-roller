import random

# Dice Roller Simulator
def dice_roller():
    print("Welcome to the Dice Roller!")
    print("You can roll a 6-sided dice. Type 'roll' to roll or 'exit' to quit.")
    
    while True:
        user_input = input("Enter your choice (roll/exit): ").strip().lower()
        if user_input == "roll":
            dice_result = random.randint(1, 6)  # Simulate rolling a 6-sided dice
            print(f"The dice rolled: {dice_result}")
        elif user_input == "exit":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Type 'roll' to roll or 'exit' to quit.")

# Run the Dice Roller
dice_roller()
