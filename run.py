from game_settings import game_settings

class GameSession:
    """
    A game session with a certain fixed number of questions
    """
    def __init__(self, n_questions):
        self.__N_QUESTIONS = n_questions
        self.__current_question = 0
        self.__correct_answers = 0
        self.__incorrect_answers = 0

    def print_summary(self):
        print("\nSummary of your game session\n----------------------------")
        print(f"Number of questions: {self.__N_QUESTIONS}")
        print(f"Number of correct answers: {self.__correct_answers}")
        print(f"Number of incorrect answers: {self.__incorrect_answers}")

class NumberOfQuestions:
    """
    A number representing the number of questions for a game session
    """
    def __init__(self):
        self.__value = None
        self.__valid = False
    
    def is_valid(self):
        return self.__valid

    def is_invalid(self):
        return not self.__valid

    def set_value(self, value):
        self.__value = value
        try:
            self.__value = int(self.__value)
        except Exception:
            return
        if self.__value < game_settings['min_n_questions']:
            return
        if self.__value > game_settings['max_n_questions']:
            return
        self.__valid = True
        
    def get_value(self):
        return self.__value

def game_loop():
    """
    This is the main loop of the game: 
    1) The user chooses the number of questions.
    2) A game session is initialized.
    3) The user plays the game session up to its end.
    4) The user can choose to play again (repeat 1,2,3,4) or exit.
    """
    play = True
    while play:
        n_questions = NumberOfQuestions()
        while n_questions.is_invalid():
            n_questions.set_value(input(
                f"\nHow many questions would you like to have in your game "
                "session?\nPlease type a number between "
                f"{game_settings['min_n_questions']} and "
                f"{game_settings['max_n_questions']}: "))

        gs = GameSession(n_questions.get_value())
        gs.print_summary()

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