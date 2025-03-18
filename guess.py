import random

def ai_guess_number():
    low, high = 0, 100
    attempts = 0
    
    print("Think of a number between 0 and 100, and AI will try to guess it!")
    input("Press Enter when you're ready...")  
    print("Game started!")
  
    
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"AI guesses: {guess}")
        
        feedback = input("Is the guess correct (c), too high (h), or too low (l)? ").strip().lower()
        
        if feedback == 'c':
            print(f"AI guessed the number in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input, please enter 'c', 'h', or 'l'.")
    else:
        print("Something went wrong! Are you sure you followed the rules?")

if __name__ == "__main__":
    ai_guess_number()
