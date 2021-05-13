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

print("Welcome to Rosk-Paper-Scissors")
player = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n")
if player == '0':
  print(rock)
elif player == '1':
  print(paper)
else:
  print(scissors)

computer = random.randint(0, 2)
if computer == 0:
  print(f"computer chose {rock}")
elif computer == 1:
  print(f"computer chose {paper}")
else:
  print(f"computer chose {scissors}")

if int(player) >= 2:
  print("You typed an  invalid number")
elif int(player) == 0 and computer == 0:
  print("You draw")
elif int(player) == 0 and computer == 1:
  print("You lost")
elif int(player) == 0 and computer == 2:
  print("You won!!!")
elif int(player) == 1 and computer == 0:
  print("You won!!!")
elif int(player) == 1 and computer == 1:
  print("You draw")
elif int(player) == 1 and computer == 2:
  print("You won!!!")
elif int(player) == 2 and computer == 0:
  print("You lost")
elif int(player) == 2 and  computer == 1:
  print("You won!!!")
elif int(player) == 2 and computer == 2:
  print("You draw")