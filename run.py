"""
Wonderful Words Game
"""

import random
from game_settings import game_settings


def game_loop():
    """
    This function implements the main loop of the game.
    Each iteration of this loop does the following:
        1) Collects the number of questions for the game session.
        2) Collects the number of options for each question.
        3) Initializes a game session.
        4) Prepares random questions and options for the game session.
        5) Plays the game session.
        6) Prints the summary of the game session.
        7) Asks the user to choose play again or exit.
    """
    play = True
    while play:
        print_header()
        n_questions = ValidValue(
            [is_numeric,
             is_greater_or_equal(game_settings['min_n_questions']),
             is_less_or_equal(game_settings['max_n_questions'])],
            int
        )
        while n_questions.is_invalid():
            n_questions.set_value(input(
                f"\nHow many questions would you like to have in your game "
                "session?\nPlease type a number between "
                f"{game_settings['min_n_questions']} and "
                f"{game_settings['max_n_questions']}:\n"))

        print_header()
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
                f"{game_settings['max_n_options']}:\n"))

        game_session = GameSession(n_questions.get_value(),
                                   n_options.get_value())
        game_session.prepare_questions()
        game_session.play()
        game_session.print_summary()

        next_step = ValidValue(
            [in_1_p_2_e_3_d], lower
        )
        while next_step.is_invalid():
            next_step.set_value(input(
                "\nPlease type:\n1 or p to play again\n2 or e to exit\n"
                "3 or d to see details\n")
            )

        if next_step.get_value() in ('2', 'e'):
            play = False

        elif next_step.get_value() in ('3', 'd'):
            game_session.print_details()
            play_again_or_exit = ValidValue(
                [in_1_p_2_e], lower
            )
            while play_again_or_exit.is_invalid():
                play_again_or_exit.set_value(input(
                    "\nPlease type:\n1 or p to play again\n2 or e to exit\n")
                )

            if play_again_or_exit.get_value() in ('2', 'e'):
                play = False

class GameSession:
    """
    A game session with a defined number of questions and a defined number
    of options per question. Each of the `n_questions` questions is a
    multiple-choice question with `n_options` possible answers. One and only
    one answer is correct, per question.
    """
    def __init__(self, n_questions, n_options):
        self.__n_questions = n_questions
        self.__n_options = n_options
        self.__n_correct_user_answers = 0
        self.__ux_list = []
        """
        The __ux_list is a list which is updated throughout a game session
        with user experience data related to that game session. This includes
        the questions, the corresponding options (i.e., the possible answers),
        the correct answer for each question and the answer chosen by the user.
        """

    def prepare_questions(self):
        """
        Prepares all the information required to provide to the user in
        a game session. This includes the questions, options available to
        choose for each question and the correct answer for each question.
        """
        print_header()
        print(f"\nI am preparing a set of {self.__n_questions} questions"
              f" for you with {self.__n_options} options per question ...")

        # Creates a list of random words to use in this game session
        words_list = random.sample(list(game_settings['game_dictionary']),
                                   self.__n_questions * self.__n_options)

        # Creates a list of `__n_questions` lists of `__n_options` words
        options_lists = [
            words_list[index: index + self.__n_options]
            for index in range(0, len(words_list),
                               self.__n_options)
        ]

        # Iterates throughout the elements that are in the options lists
        # (each element is a list itself) and fills the user experience list
        # with what is possible at this moment.
        question_number = 1
        for options_list in options_lists:
            correct_answer = options_list[0]
            question = f'{game_settings["game_dictionary"][options_list[0]]}'
            random.shuffle(options_list)
            self.__ux_list.append(
                {
                    "question_number": question_number,
                    "question": question,
                    "correct_answer": correct_answer,
                    "options": options_list,
                    "user_answer": None
                }
            )
            question_number += 1
        print("\nQuestions prepared.")
        input("\nPress enter to start the game session.\n")

    def play(self):
        """
        Runs the game, asking the user all the questions, one at a time.
        The main objective here is to collect the user answer for each
        question that is in each element of the `__ux_list` list.
        """
        for ux_element in self.__ux_list:
            ux_element["user_answer"] = collect_user_answer(ux_element, self.__n_questions)
            if ux_element["user_answer"] == ux_element["correct_answer"]:
                self.__n_correct_user_answers += 1

    def print_summary(self):
        """
        Prints the summary of this game session
        """
        print_header()
        print("\nSummary of your game session\n----------------------------")
        print(f"Number of questions: {self.__n_questions}")
        print(f"Correct answers: {self.__n_correct_user_answers}")

    def print_details(self):
        """
        Prints the detailed information about the game session
        """
        for ux_element in self.__ux_list: 
            print_header()
            print("\nDetails of your game session"
                  "\n----------------------------")
            print(f'\nQuestion {ux_element["question_number"]} of'
                  f' {self.__n_questions}: What is the word for "'
                  f'{ux_element["question"]}" ?')
            print(f'\nCorrect answer: {ux_element["correct_answer"]}')
            thumbs_up_if_correct = 3 * "\U0001F44D" \
                if ux_element["correct_answer"] == ux_element["user_answer"] \
                else ""
            print(f'\nYour answer: {ux_element["user_answer"]} '
                  f'{thumbs_up_if_correct}')
            if ux_element["question_number"] != self.__n_questions:
                input("\nPress enter to continue.\n")

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
            if not validator(value):
                self.__valid = False
                return
        self.__valid = True
        self.__value = self.__converter(value)
        
    def get_value(self):
        return self.__value

def print_header():
    print("\033[H\033[J")  # to clear the screen
    print(80 * '-')
    print(f"{5 * ' '}Wonderful Words game using the"
          f" \"{game_settings['game_dictionary_name']}\" "
          "dictionary")
    print(80 * '-')


def collect_user_answer(ux_element, n_questions):
    """
    Presents a question with the possible options for the user to answer
    and collects the user answer.
    """
    print_header()
    print(f'\nQuestion {ux_element["question_number"]} of {n_questions}:')
    print('\nWhat is the word for ...')
    print(f'\n"{ux_element["question"]}" ?\n')
    for i in range(0, len(ux_element["options"])):
        print(f'{i+1} - {ux_element["options"][i]}')

    answer_to_game_question = ValidValue(
            [is_numeric,
             is_greater_or_equal(1), 
             is_less_or_equal(len(ux_element["options"]))], int
    )
    while answer_to_game_question.is_invalid():
        answer_to_game_question.set_value(input(
            f'\nPlease type a number between 1 and'
            f' {len(ux_element["options"])}:\n')
        )
    return(ux_element["options"][answer_to_game_question.get_value()-1])


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

def in_1_p_2_e(value):
    if value.lower() in ('1', 'p', '2', 'e'):
        return True
    return False

def in_1_p_2_e_3_d(value):
    if value.lower() in ('1', 'p', '2', 'e', '3', 'd'):
        return True
    return False

def lower(value):
    return value.lower()

game_loop()
