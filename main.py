# Description:
# This script represents a student's first and horrendous attempt at creating a supposedly simple Python program.
# Note that this means that the code will be poorly structured and contains inefficient processing. 
# The program is likely to contain numerous bugs that may or may not highly impact user experience.
# Please do not heavily criticize the code, as it is meant to be a learning exercise for me (talking to future me).
# This code is supposed to be a game that requires the player to solve puzzles to progress through levels.

# Creator: Deltrix99
# Date: July 10, 2025 - Present
# Version: 1.0

# essential / widespread imports and libraries
import sys
import math
import random
import time


# custom imports from separate files:

# saving system
from saves import save_current, load_current, save_update

# level system
from levels import level_selected

# main function: the main entry point of the game
def main():
    print("Welcome to the Deltrix's Puzzle Game!")
    print("Solve difficult puzzles to progress through increasingly challenging levels.")
    print("These puzzles will consist of random topics of my choosing.")

    try:

        if sys.argv[1:]:
            player_name = sys.argv[1]
            print(f"Welcome back, {player_name}!")
            level, total_time, player_name = load_current(player_name)
    
        else:
            player_name = input("Enter your name to start the game: ")
            print(f"Hello, {player_name}! Let's begin this stupid game!")
            level = 1
            total_time = 0.0
    
    except IndexError:
        sys.exit("No player name provided. Please run the game with your name as an argument or start a new game.")
    
    # starts the game along with the timer
    game_start_time = time.time()
    
    while True:
        print(f"\nYou are currently on Level {level}.")
        print("Solve the puzzle to progress to the next level.")
        
        level_selected(level)
        
        level_end_time = time.time()
        level_elapsed = level_end_time - game_start_time
        print(f"Congratulations! You solved Level {level} in {level_elapsed:.2f} seconds.")
        total_time += level_elapsed
        
        next_level = input("Do you want to proceed to the next level? (yes/no): ").strip().lower()
        
        if next_level != 'yes':
            
            save_after_completion = input("Thank you for playing! Would you like to save your progress? (add/update/none): ").strip().lower()
            
            if save_after_completion == 'add':
                save_current(level, total_time, player_name)
                print(f"Your progress has been added as a new save for Level {level}.")
            
            elif save_after_completion == 'update':
                save_update(player_name, level, total_time)
                print(f"Your save has been updated for Level {level}.")
            
            else:
                print("No save action taken.")
            print(f"Total time spent on all levels so far: {total_time:.2f} seconds.")
            break
        
        else:
            save_choice = input("Do you want to add a new save or update your previous save? (add/update): ").strip().lower()
            
            if save_choice == 'add':
                save_current(level, total_time, player_name)
                print(f"Your progress has been added as a new save for Level {level}.")
            
            elif save_choice == 'update':
                save_update(player_name, level, total_time)
                print(f"Your save has been updated for Level {level}.")
            
            else:
                print("No save action taken.")
        
        level += 1
        game_start_time = time.time()





if __name__ == "__main__":
    main()

