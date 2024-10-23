from brain_even import dialog_with_user
from brain_even import main

def test_dialog_with_user():
    dialog_with_user('welcome')  #Welcome to the Brain Games!
    name = dialog_with_user('hellow')  #May I have your name? Sam
                                       #Hello, Sam!
    dialog_with_user('rules')  #Answer "yes" if the number is even, otherwise answer "no".
    dialog_with_user('question', '15')  #Question: 15
    dialog_with_user('answer', 'no')  #Your answer: no
    dialog_with_user('correct')  #Correct!
    dialog_with_user('greeting', name)  #Congratulations, Sam!


#test_dialog_with_user()
main()