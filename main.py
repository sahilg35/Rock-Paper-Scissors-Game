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

#Write your code below this line 👇
list = [rock,paper,scissors]
me = int(input("Choose a random number, 0 for rock, 1 for paper, 2 for scissors:\n "))
if me > 2 or me < 0:
  print("You choose a invalid number")
else:
  print(list[me])
number = random.randint(0,2)
computer = list[number]
print(f"Computer choose {computer}")

if me > 2 or me < 0:
  print("You choose a invalid number")
elif me == 2 and number == 0:
  print("You loss")
elif me == 0 and number == 2:
  print("You Win")
elif me > number:
  print("You Win")
elif number > me:
  print("You loss")
elif me == number:
  print("It's a draw")