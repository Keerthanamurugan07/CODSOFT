import random
import tkinter as tk

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def on_choice(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    lbl_result.config(text=result)
    lbl_user_choice.config(text=f"You chose: {user_choice}")
    lbl_computer_choice.config(text=f"Computer chose: {computer_choice}")
    update_score(result)

def update_score(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    lbl_score.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

def play_again():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    lbl_score.config(text="Score - You: 0, Computer: 0")

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create widgets
lbl_result = tk.Label(root, text="")
lbl_user_choice = tk.Label(root, text="")
lbl_computer_choice = tk.Label(root, text="")
lbl_score = tk.Label(root, text="Score - You: 0, Computer: 0")

btn_rock = tk.Button(root, text="Rock", command=lambda: on_choice("rock"))
btn_paper = tk.Button(root, text="Paper", command=lambda: on_choice("paper"))
btn_scissors = tk.Button(root, text="Scissors", command=lambda: on_choice("scissors"))
btn_play_again = tk.Button(root, text="Play Again", command=play_again)
btn_quit = tk.Button(root, text="Quit", command=root.quit)

# Arrange widgets
lbl_result.pack()
lbl_user_choice.pack()
lbl_computer_choice.pack()
lbl_score.pack()

btn_rock.pack(side=tk.LEFT, padx=5, pady=5)
btn_paper.pack(side=tk.LEFT, padx=5, pady=5)
btn_scissors.pack(side=tk.LEFT, padx=5, pady=5)
btn_play_again.pack(side=tk.LEFT, padx=5, pady=5)
btn_quit.pack(side=tk.LEFT, padx=5, pady=5)

# Start the event loop
root.mainloop()
