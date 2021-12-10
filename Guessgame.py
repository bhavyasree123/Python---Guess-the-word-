import random

user_name = input('Good name,Please! : ')
print('HELLO!' , user_name)
words = ['grapes' , 'strawberry' , 'watermelon' , 'kiwi' ,'orange']
c = random.choice(words)
print(c)
user_turns = 12
while user_turns > 0:
    failed = 0
    user_choice = input('Enter your character : ')
    if user_choice in c:
        print(user_choice,"it's there")
    else:
        print('wrong')
        failed += 1
        print(failed,'you have')
    
    continue  
    

    
    