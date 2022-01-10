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
        self.__history = []

    def play(self):
        """
        Runs an entire game session, asking the user all the questions, one
        after another. The relevant data for the game session is kept in
        memory in this instance of the game session.
        """
        if self.__current_question != 0:
            # impossible situation unless there is an error in the code
            print("\nThis game session is already going on or it has ended "
                  "and cannot be replayed.")
            return
        for self.__current_question in range(1, 1+self.__N_QUESTIONS):
            print(f'\nQuestion {self.__current_question}:\nWhat is the word for'
                  ' "..."?\n')

    def print_summary(self):
        print("\nSummary of your game session\n----------------------------")
        print(f"Number of questions: {self.__N_QUESTIONS}")
        print(f"Number of correct answers: {self.__correct_answers}")
        print(f"Number of incorrect answers: {self.__incorrect_answers}")

class NumberOfQuestions:
    """
    A number representing the number of questions for a game session.
    This class is used to validate the value for number of questions
    provided by the user.
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
    This function implements the main loop of the game. Each iteration of
    this loop does the following:
    1) Collects and validates the number of questions to be included in
       the next game session.
    2) Initializes a game session.
    3) ...
    4) Asks the user if they want to play again or exit.

    This function loops, repeating the steps 1 to 4 above, until the user
    answers in step 4 to exit.
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

        game_session = GameSession(n_questions.get_value())
        game_session.play()
        game_session.print_summary()

        user_answer = None
        while user_answer not in ('1', '2'):
            user_answer = input("\nPlease type 1 to play again or 2 to "
                                "exit: ")
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