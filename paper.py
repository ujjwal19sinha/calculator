import random
user_choice = input('choose your weapon[rock ,paper,scissor]:')
computer_choice = random.choice(['rock' ,'paper','scissor'])
user_choice=user_choice.lower()
print(user_choice,computer_choice)
if user_choice =='rock' and computer_choice == 'rock':
    print('Draw')
elif user_choice == 'rock' and computer_choice == 'scissor':
     print('USER Won')
elif user_choice == 'rock' and computer_choice == 'paper':
    print('Computer won')
elif user_choice == 'scissor' and computer_choice == 'scissor':
    print('Draw')
elif user_choice == 'scissor' and computer_choice == 'rock':
    print('Computer won')
elif user_choice == 'scissor' and computer_choice == 'paper':
    print('User Won')
elif user_choice == 'paper' and computer_choice == 'paper':
    print('Draw')
elif user_choice == 'paper' and computer_choice == 'scissor':
    print('Computer Won')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('User won')
else:
    print("invalid case")    
