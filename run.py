from game_settings import game_settings
from pprint import pprint
import random

class GameSession:
    """
    A game session with a certain fixed number of questions
    """
    def __init__(self, n_questions, n_options):
        self.__n_questions = n_questions
        self.__n_options = n_options
        self.__correct_answers = 0
        self.__ux_list = []


    def prepare_questions(self):
        """
        Prepares all the information required to provide to the user in
        a game session. This includes the questions, options available to
        choose for each question and the correct answer for each question.
        """
        print("\nI am preparing the questions for your game session...")

        # Creates a list of words to use in this session
        words_list = random.sample(
            list(game_settings['game_dictionary']), self.__n_questions *
            self.__n_options
        )

        # Creates a list of lists of words (each word is an option)
        options_lists = [
            words_list[index: index + self.__n_options]
            for index in range(0, len(words_list),
                               self.__n_options)
        ]

        # Iterates the options lists and fills the user experience list
        # for this session, with everything we can at this moment
        for options_list in options_lists:
            correct_answer = options_list[0]
            question = f'Question {1 + len(self.__ux_list)}: What is the word'\
                       f' for "'\
                       f'{game_settings["game_dictionary"][options_list[0]]}" ?'
            random.shuffle(options_list)
            self.__ux_list.append(
                {
                    "question": question,
                    "correct_answer": correct_answer,
                    "options": options_list,
                    "user_answer": None
                }
            )
        print("Questions prepared.")

    def play(self):
        """
        Runs an entire game session, asking the user all the questions, one
        at a time. The relevant data for the game session is updated in this
        object's instance
        """
        for ux_element in self.__ux_list:
            ux_element["user_answer"] = collect_user_answer(ux_element)

    def print_summary(self):
        #print("\nSummary of your game session\n----------------------------")
        #print(f"Number of questions: {self.__n_questions}")
        #print(f"Number of correct answers: {self.__correct_answers}")
        pprint(self.__ux_list)

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

def collect_user_answer(ux_element):
    """
    Presents a question with the possible options for to the user to answer
    and collects the user answer.
    """
    print(f'\n{ux_element["question"]}')
    for i in range(0, len(ux_element["options"])):
        print(f'{i+1} - {ux_element["options"][i]}')
    user_answer = input(f'Please type a number between 1 and '
                        f' {len(ux_element["options"])}: ')
    return(ux_element["options"][int(user_answer)-1])

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

        game_session = GameSession(n_questions.get_value(), 5)
        game_session.prepare_questions()
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



