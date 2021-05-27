import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

human = int(input("1 for paper,0 for rock and 2 for scissors\n"))
print(game_images[human])

computer = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer])

if human >= 3 or human < 0:
    print("You typed an invalid number, you lose!")
elif human == 0 and computer == 2:
    print("You win!")
elif computer == 0 and human == 2:
    print("You lose")
elif computer > human:
    print("You lose")
elif human > computer:
    print("You win!")
elif computer == human:
    print("It's a draw")
