import json

def read_dictionary_file(filename):
    """
    Reads a file that contains a dictionary.
    Returns the dictionary loaded into a dict object.
    """
    try:
        with open(filename, "r") as file:
            dict_str = file.read()
        loaded_dict = json.loads(dict_str)
        return loaded_dict
    except Exception:
        print(f"\nError when reading the {filename} file.\nPlease contact the Support Team.\n")
        raise

print("Welcome to the Wonderful Words game!\n")

print("Loading game settings...")
game_settings = read_dictionary_file("game_settings.dict")
print("Game settings loaded.")
print(f"Game Dictionary Name: \"{game_settings['game_dictionary_name']}\".\n")

print(f"Loading the \"{game_settings['game_dictionary_name']}\" dictionary...")
game_dictionary = read_dictionary_file("game_dictionary.dict")
print(f"\"{game_settings['game_dictionary_name']}\" dictionary loaded.\n")

print("I just need to ask you two questions and the game will start!")
player_name = input("\nWhat is your name?\n")
n_questions = input(
    "\nHow many questions would you like to have in your game session"
    f" ({game_settings['minimum_number_of_questions_per_game_session']} to "
    f" {game_settings['maximum_number_of_questions_per_game_session']})?\n")

print(f"\n{player_name}, I am starting a new game session with "
      f"{n_questions} questions for you...")