import random

user_name = input('Good name,Please! : ')
print('HELLO!' , user_name)
words = ['grapes' , 'strawberry' , 'watermelon' , 'kiwi' ,'orange']
c = random.choice(words)
print(c)
while True:
    user_choice = input('Enter your character : ')
    for word in c:
        print(word)
    if user_choice in c:
        print(user_choice,"it's there")
    else:
        print('wrong')
    user_turns = 12
    if user_turns <= 12:
        continue
    elif user_turns > 12:
        quit()