def dialog_with_user(request: str, *var_request):
    import prompt
    match request:
        case 'welcome':
            print('Welcome to the Brain Games!')
        case 'hellow':
            name = prompt.string('May I have your name? ')
            print(f'Hello, {name}!')
            return name
        case 'rules_even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'rules_calc':
            print('What is the result of the expression?')
        case 'rules_gcd':
            print('Find the greatest common divisor of given numbers.')
        case 'rules_progressions':
            print('What number is missing in the progression?')
        case 'rules_prime':
            print('Answer "yes" if given number is prime.'
                  ' Otherwise answer "no".')
        case 'question':
            print(f'Question: {var_request[0]}')
        case 'answer':
            answer = prompt.string('Your answer: ')
            return answer
        case 'correct':
            print('Correct!')
        case 'wrong':
            print(f"'{var_request[0]}' is wrong answer ;"
                  f"(. Correct answer was '{var_request[1]}'.")
            print(f"Let's try again, {var_request[2]}!")
        case 'greeting':
            print(f'Congratulations, {var_request[0]}!')


def is_wrong_for_even(number_for_ask: int, answer: str, name: str):
    if number_for_ask % 2 != 0 and answer != 'no':
        wrong_answer: str = answer
        correct_answer: str = 'no'
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
        wrong_answer: str = answer
        correct_answer: str = string_for_ask
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    else:
        return False


def is_wrong_for_gcd(string_for_ask: tuple, answer: str, name: str) -> bool:
    min_number: int = min(string_for_ask)
    max_number: int = max(string_for_ask)
    dividers: list[int] = list(range(min_number, 0, -1))
    divider: int = 0
    for divider in dividers:
        """
        look for first common divider:
        """
        if min_number % divider == 0 and max_number % divider == 0:
            break
    if answer != str(divider):
        wrong_answer: str = answer
        correct_answer: str = str(divider)
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    else:
        return False


def is_wrong_for_progression(gap_value: str, answer: str, name: str) -> bool:
    if answer != gap_value:
        wrong_answer = answer
        correct_answer = gap_value
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    else:
        return False


def is_wrong_for_prime(number_for_ask: int, answer: str, name: str) -> bool:
    is_prime: bool = True
    for divider in range(2, number_for_ask // 2):
        if number_for_ask % divider == 0:
            is_prime = False
            break
    if is_prime is False and answer != 'no':
        wrong_answer: str = answer
        correct_answer: str = 'no'
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    elif is_prime is True and answer != 'yes':
        wrong_answer: str = answer
        correct_answer: str = 'yes'
        dialog_with_user('wrong', wrong_answer, correct_answer, name)
        return True
    else:
        return False
