import random

user_name = input('Good name,Please! : ')
print('HELLO!' , user_name)
words = ['grapes' , 'strawberry' , 'watermelon' , 'kiwi' ,'orange']
c = random.choice(words)
guesses = ''
user_turns = 12
while user_turns > 0:
    failed = 0
    for char in c:
        if char in guesses:
            print(char)
        else:
            print('-')
            failed += 1
    if failed == 0:
        print('You win')
        print('the word is',c)
        break
    guess = input("guess the character: ")
    guesses += guess
    if guess not in c:
        user_turns -= 1
        print("Soory! It's wrong")
        print('You have',user_turns,'Chances')
        if user_turns==0:
            print('you LOSE')


