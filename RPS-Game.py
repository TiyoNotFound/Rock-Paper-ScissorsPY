import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def get_ai_choice(history, difficulty):
    if difficulty == "easy":
        return random.choice(["rock", "paper", "scissors"])
    elif difficulty == "balanced":
        return random.choice(["rock", "paper", "scissors"] * 2)
    elif difficulty == "hard":
        if len(history) >= 3:
            user_sequence = "".join(history[-3:])
            for combo in [("rock", "paper"), ("rock", "scissors"), ("paper", "scissors")]:
                if combo[0] in user_sequence and combo[1] in user_sequence:
                    return combo[1]
        if random.random() < 0.05:
            return random.choice(["rock", "paper", "scissors"])
        return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, ai):
    if user == ai:
        return "It's a tie!"
    elif (user == "rock" and ai == "scissors") or (user == "scissors" and ai == "paper") or (user == "paper" and ai == "rock"):
        return "You win!"
    return "AI wins!"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    difficulty = input("Choose AI difficulty (Easy, Balanced, Hard): ").lower()
    user_history = []
    
    while True:
        user_choice = get_user_choice()
        user_history.append(user_choice)
        ai_choice = get_ai_choice(user_history, difficulty)
        
        print(f"You choose {user_choice}")
        print(f"CPU choose {ai_choice}")
        
        result = determine_winner(user_choice, ai_choice)
        print(result)
        
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
