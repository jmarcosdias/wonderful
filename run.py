from game_settings import game_settings
from pprint import pprint
import random


def game_loop():
    """
    This function implements the main loop of the game.
    Each iteration of this loop does the following:
        1) Collects the number of questions for the game session.
        2) Collects the number of options for each question.
        3) Initializes a game session.
        4) Prepares the questions for the game session.
        5) Plays the game session.
        6) Prints the summary of the game session.
        7) Asks the user to play again or exit.
    """
    play = True
    while play:
        n_questions = ValidValue(
            [is_numeric,
             is_greater_or_equal(game_settings['min_n_questions']),
             is_less_or_equal(game_settings['max_n_questions'])],
            int
        )
        while n_questions.is_invalid():
            n_questions.set_value(input(
                f"\nHow many questions would you like to see in your game "
                "session?\nPlease type a number between "
                f"{game_settings['min_n_questions']} and "
                f"{game_settings['max_n_questions']}: "))
        
        n_options = ValidValue(
            [is_numeric,
             is_greater_or_equal(game_settings['min_n_options']),
             is_less_or_equal(game_settings['max_n_options'])],
            int
        )
        while n_options.is_invalid():
            n_options.set_value(input(
                f"\nHow many options would you like to see for each question?"
                "\nPlease type a number between "
                f"{game_settings['min_n_options']} and "
                f"{game_settings['max_n_options']}: "))

        game_session = GameSession(n_questions.get_value(),
                                   n_options.get_value())
        game_session.prepare_questions()
        game_session.play()
        game_session.print_summary()

        play_again_or_exit = ValidValue(
            [is_numeric, is_greater_or_equal(1), is_less_or_equal(2)], int
        )
        while play_again_or_exit.is_invalid():
            play_again_or_exit.set_value(input(
                "\nPlease type 1 to play again or 2 to exit: ")
            )

        if play_again_or_exit.get_value() == 2:
            play = False


class GameSession:
    """
    A game session with a certain fixed number of questions
    """
    def __init__(self, n_questions, n_options):
        self.__n_questions = n_questions
        self.__n_options = n_options
        #self.__correct_answers = 0
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


class ValidValue:
    """
    Class for a value that is considered valid or invalid.
    The constructor receives: 
        1) validators, which is an array of functions to validate the value.
        2) converter, which is a function to convert the value in case it is
           valid.
    """
    def __init__(self, validators, converter):
        self.__value = None
        self.__valid = None
        self.__validators = validators
        self.__converter = converter
    
    def is_valid(self):
        return self.__valid

    def is_invalid(self):
        return not self.__valid

    def set_value(self, value):
        for validator in self.__validators:
            pprint(validator)
            if not validator(value):
                print("not valid")
                self.__valid = False
                return
        self.__valid = True
        self.__value = self.__converter(value)
        
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

def is_numeric(value):
    return value.isnumeric()

def is_greater_or_equal(value1):
    def is_greater_or_equal_inner(value2):
        return int(value2) >= value1
    return is_greater_or_equal_inner

def is_less_or_equal(value1):
    def is_less_or_equal_inner(value2):
        return int(value2) <= value1
    return is_less_or_equal_inner

print("\nWelcome to the Wonderful Words game!")
print(f"\nThis game's dictionary is:"
      f" \"{game_settings['game_dictionary_name']}\".")
game_loop()
