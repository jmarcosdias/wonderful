# Wonderful Words Game

## User's Goal

The users of the <em>Wonderful Words Game</em> want to play an online multiple-choice quiz game that will enrich their vocabulary with unusual words.

## Target Audience

The <em>Wonderful Words Game</em> is targeted to adults who are word lovers and have fun with learning new words.

## Owner's Goal

The goal of the <em>Wonderful Words Game</em> is to entertain people and foster the learning of new words. 

## Description of the Game

In each game session, the user will be asked a series of questions. Each question will have a number of options to choose from. 

The number of questions and number of options are defined by the user before the session starts. 

For each question, only one option is correct.

Below is a screenshot where a question number 7 is presented to the user along with the options the user can choose. This screenshot was taken from a game session with 10 questions and 6 options per question.

![Mockup Image](assets/doc-images/mockup.png)

After the last question, a summary of the game session is presented. At this point, the user can choose to play again, exit or see the details.

![Game Session Summary](assets/doc-images/summary-of-the-game-session-1.png)

The details consist in presenting each question again, along with the correct answer and the user's answer.

![Game Session Summary](assets/doc-images/question-correct-answer-details.png)

![Game Session Summary](assets/doc-images/question-wrong-answer-details.png)

## Features 

### Existing Features

#### The starting screen

A welcome message and an introductory explanation is presented to the user.

![Feature Starting Screen](assets/doc-images/starting-screen.png)

- Ability to choose the number of questions

The user can choose the number of questions in a game session. 

![Feature Choose Number of Questions](assets/doc-images/ability-to-choose-number-of-questions.png)

The possible values are in the `[min_n_questions, max_n_questions]` integer interval that is defined in the object pointed by the game_settings variable in the game_settings.py file.

    game_settings = {
        ...
        "min_n_questions": 1,
        "max_n_questions": 10,
        ...
    }

#### Ability to choose the number of options

The user can choose the number of options that will be made available per question in a game session.

![Feature Choose Number of Options](assets/doc-images/ability-to-choose-number-of-options.png)

The possible values are in the `[min_n_options, max_n_options]` integer interval that is defined in the object pointed by the game_settings variable in the game_settings.py file.

    game_settings = {
        ...
        "min_n_options": 2,
        "max_n_options": 6,
        ...
    }

#### Preparation of questions and corresponding options to answer

For each game session, the program randomically picks up the set of questions and options to answer those questions.

![Preparation of Questions and Options](assets/doc-images/preparation-of-questions-and-options-to-answer.png)

The questions and options to answer are picked up from the dictionary that is defined in the object pointed by the game_settings variable in the game_settings.py file.

    game_settings = {
        ...
        "game_dictionary": {
            ....
        }
    }

#### Present a question and collect the answer

Along the game session, each questions is presented with the corresponding options to answer and then the answer is collected.

![Present Question Collect Answer](assets/doc-images/present-a-question-and-collect-the-answer.png)

The answer is kept in memory in the object pointed by the user experience list (`__ux_list`) instance variable of the GameSession class.

Below is an example of possible contents of `__ux_list` at the end of a game session with 2 questions and 2 options per question. In this example, the user got the first question wrong and the second question right.

    [
        {
            'question_number': 1,
            'question': 'the hybrid off spring of a male tiger and a lioness (the offspring of a male lion and a tigress being a liger)',
            'correct_answer': 'tigon',
            'options': ['struthious', 'tigon'],
            'user_answer': 'struthious'
        }, 
        {
            'question_number': 2,
            'question': 'the practice of registering well-known names as Internet domain names, in the hope of reselling them at a profit',
            'correct_answer': 'cybersquatting',
            'options': ['cupreous', 'cybersquatting'],
            'user_answer': 'cybersquatting'
        }
    ]

#### Summary of the game session

The summary is presented after the last question.

![Game Session Summary](assets/doc-images/summary-of-the-game-session-1.png)

#### Details of the game session

If the user selects the details option, after the session summary, the details are presented. 

The details consist in presenting all the questions again, one at a time, with the correct answer and the user answer.

![Game Session Summary](assets/doc-images/details-of-the-game-session-1.png)

After the last question presented in the details, the user can choose to play again or exit.

![Game Session Summary](assets/doc-images/details-of-the-game-session-2.png)

### Future Features

In a future release, the following feature is planned to be implemented.

#### Ability to choose the dictionary

Currently, only one dictionary is used along this game. The user has no option to choose the dictionary.

In the current version, there is only the "Weird And Wonderful Words" dictionary, which is great, but is not good for all purposes. For example this dictionary is not good for beginners or for children.

The current structure of the game settings is as follows.

    game_settings = {
        "game_dictionary_name": "Weird And Wonderful Words",
        "min_n_questions":1,
        "max_n_questions":10,
        "min_n_options":2,
        "max_n_options":6,
        "game_dictionary": {
            "word-1": "description-1",
            "word-2": "description-2",
            ...
            "word-n": "description-n"
        }
    }

A future version of this game is planned to accomodate different dictionaries.

In this future version, the structure of the game settings will be as shown below.

    game_settings = {
       "min_n_questions":1,
       "max_n_questions":10,
       "min_n_options":2,
       "max_n_options":6,
       "dictionaries":[
          {
             "dictionary_name":"Weird And Wonderful Words",
             "game_dictionary":{
                "word-1":"description-1",
                "word-2":"description-2",
                "word-n":"description-n"
             }
          },
          {
             "dictionary_name":"Basic English Dictionary",
             "game_dictionary":{
                "word-1":"description-1",
                "word-2":"description-2",
                "word-n":"description-n"
             }
          },
          {
             "dictionary_name":"Children English Dictionary",
             "game_dictionary":{
                "word-1":"description-1",
                "word-2":"description-2",
                "word-n":"description-n"
             }
          }
       ]
    }

By using the above structure, it will be possible to adapt the python code for this game so that the user will be able to choose the dictionary at runtime.

## Testing 

## Validate Correctness

The tests in this section are to validate the correctness of questions and options presented to the user and the correctness of the evaluation of the answers.

Test Conditions:
1. All questions and options must be taken from the game dictionary. 
1. There must be only one correct answer. 
1. When the user selects the correct answer, the game must consider this answer correct.
1. When the user selects an incorrect answer, the game must not consider this answer correct. 

Based on the https://www.lexico.com/explore/weird-and-wonderful-words dictionary, a series of game sessions was played and all the answers were validated against the dictionary. No errors were found.

Below are some examples of the tests that were conducted, with different numbers of questions and different numbers of options. In these examples, a game with X questions and Y options per question is referred as an X/Y game.

### Question in a 10/3 game

User selects the correct answer. Conditions 1, 2 and 3 must be satisfied.

Correct answer is 'decubitus'.

![Correctness Test Example 1a](assets/doc-images/correctness-testing-example-1a.png)

![Correctness Test Example 1b](assets/doc-images/correctness-testing-example-1b.png)

![Correctness Test Example 1c](assets/doc-images/correctness-testing-example-1c.png)

Result: Success.

Details: User selected correct answer. Conditions 1, 2 and 3 were verified.

### Question in a 10/6 game

User selects an incorrect answer. Conditions 1, 2 and 4 must be satisfied.

Correct answer is 'afreet'.

![Correctness Test Example 2a](assets/doc-images/correctness-testing-example-2a.png)

![Correctness Test Example 2b](assets/doc-images/correctness-testing-example-2b.png)

![Correctness Test Example 2c](assets/doc-images/correctness-testing-example-2c.png)

Result: Success.

Details: User selected incorrect answer. Conditions 1, 2 and 4 were verified.

### Question in a 1/1 game

User selects an incorrect answer. Conditions 1, 2 and 4 must be satisfied.

Correct answer is 'higgler'.

![Correctness Test Example 3a](assets/doc-images/correctness-testing-example-3a.png)

![Correctness Test Example 3b](assets/doc-images/correctness-testing-example-3b.png)

![Correctness Test Example 3c](assets/doc-images/correctness-testing-example-3c.png)

Result: Success.

Details: User selected incorrect answer. Conditions 1, 2 and 4 were verified.

## Validate Summary of the Game


## Validate User Input

These tests are to ensure that a distracted or misbehaving user will not break the game.