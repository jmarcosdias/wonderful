from game_settings import game_settings

class GameSession:
    """
    A game session with a certain number of questions
    """
    def __init__(self, n_questions):
        self.__n_questions = n_questions
        self.__current_question = 0
        self.__correct_answers = 0
        self.__incorrect_answers = 0

    def print_summary(self):
        print("\nSummary of your game session\n----------------------------")
        print(f"Number of questions: {self.__n_questions}")
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
    A game session is initialized and carried out up to its end. The user is
    then asked if they would like to play again or exit. This repeats
    consecutively until the user answers they want to exit.
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