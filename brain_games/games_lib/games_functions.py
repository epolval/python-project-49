def dialog_with_user(request: str, *var_request):
    import prompt
    match request:
        case 'welcome':
            print('Welcome to the Brain Games!')
        case 'hellow':
            name = prompt.string('May I have your name? ')
            print(f'Hellow, {name}!')
            return name
        case 'rules_even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'rules_calc':
            print('What is the result of the expression?')
        case 'question':
            print(f'Question: {var_request[0]}')
        case 'answer':
            answer = prompt.string('Your answer: ')
            return answer
        case 'correct':
            print('Correct!')
        case 'wrong':
            print(f"{var_request[0]} is wrong answer;"
                  f"(.Correct answer was {var_request[1]}.")
            print(f"Let's try again, {var_request[2]}!")
        case 'greeting':
            print(f'Congratulations, {var_request[0]}!')


def is_wrong_for_even(number_for_ask: int, answer: str, name: str):
    if number_for_ask % 2 != 0 and answer != 'no':
        wrong_answer = answer
        correct_answer = 'no'
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    elif number_for_ask % 2 == 0 and answer != 'yes':
        wrong_answer = answer
        correct_answer = 'yes'
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    else:
        return False


def is_wrong_for_calc(string_for_ask: int, answer: str, name: str):
    if answer != str(string_for_ask):
        wrong_answer = answer
        correct_answer = string_for_ask
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    else:
        return False
