# This script saves the current game state to a CSV file.
# It allows the player to save their progress, including the current level and time taken.
# The saved data can be used to resume the game later or for tracking progress.

# main function: for testing purposes
def main():
    level = int(input("Enter the test level:"))
    time = float(input("Enter the time taken so far: "))
    save = input("Enter your name for saving progress: ")
    save_current(level, time, save)



# save_current function: saves the current game state to a CSV file
def save_current(level, time, save):
    save_path = "saves.csv"
    
    try:
        write_header = False
        try:
            with open(save_path, "r") as saved_file:
                if saved_file.read().strip() == "":
                    write_header = True
        except FileNotFoundError:
            write_header = True
        
        with open(save_path, "a") as save_file:
            if write_header:
                save_file.write("Level,Score,Player\n")
            
            save_file.write(f"{level},{time},{save}\n")
        
        print(f"Game state saved successfully to {save_path}!")
    
    except Exception as e:
        print(f"Failed to save game state: {e}")



# load_current function: loads the current game state from a CSV file if it exists.
def load_current(player_name):
    save_path = "saves.csv"
    
    try:
        with open(save_path, "r") as saved_file:
            lines = saved_file.readlines()
            
            if len(lines) <= 1:
                print("No saved game found.")
                return None
            
            for line in reversed(lines[1:]):  # skip header
                parts = line.strip().split(",")
                
                if len(parts) == 3 and parts[2] == player_name:
                    level = int(parts[0])
                    time = float(parts[1])
                    player = parts[2]
                    print(f"Loaded game state: Level {level}, Time {time}, Player {player}")
                    return level, time, player
            
            print(f"No saved game found for player '{player_name}'.")
            return None
    
    except FileNotFoundError:
        print("No saved game found.")
        return None
    except Exception as e:
        print(f"Failed to load game state: {e}")
        return None



# save_update function: updates the game state for a specific player in the CSV file.
def save_update(player_name, new_level, new_time):
    save_path = "saves.csv"
    updated = False
    
    try:
        with open(save_path, "r") as saved_file:
            lines = saved_file.readlines()
            
            if len(lines) <= 1:
                print("No saved game found to update.")
                return
            
            with open(save_path, "w") as save_file:
                save_file.write(lines[0])
                for line in lines[1:]:
                    parts = line.strip().split(",")
                    
                    if len(parts) == 3 and parts[2] == player_name:
                        save_file.write(f"{new_level},{new_time},{player_name}\n")
                        updated = True
                    else:
                        save_file.write(line)
        
        if updated:
            print(f"Game state for '{player_name}' updated successfully in {save_path}!")
        else:
            print(f"No save found for player '{player_name}' to update.")
    
    except Exception as e:
        print(f"Failed to update game state: {e}")


if __name__ == "__main__":
    main()