from game_settings import game_settings

class GameSession:
    def __init__(self, n_questions):
        self.n_questions = n_questions

def game_loop():
    """
    A game session is initialized and carried out up to its end. The user is then
    asked if they would like to play again or exit. This repeats consecutively 
    until the user answers they want to exit.
    """
    play = True
    while play:
        n_questions = input(
            f"\nHow many questions would you like to have in your game session ("
            f"{game_settings['min_n_questions']} to "
            f"{game_settings['max_n_questions']})?\n")

        GameSession(n_questions)

        user_answer = None
        while user_answer not in ('1', '2'):
            user_answer = input("\nPlease type 1 to play again or type 2 to "
                                "exit\n")
            if user_answer == '2':
                play = False

def main():
    """
    Run the game loop.
    """
    game_loop()

print("\nWelcome to the Wonderful Words game!")
print(f"\nThis game's dictionary is: \"{game_settings['game_dictionary_name']}\".")
main()