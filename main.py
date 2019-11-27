import random

score = 0

def roll():
    global score
    a = 0
    print("Roll the dice by typing: roll")
    ifdice = input()
    if ifdice == "roll":#this sets the dice to random numbers from 1 to 6
      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
      dice3 = random.randint(1,6)
      dice4 = random.randint(1,6)
      dice5 = random.randint(1,6)
    print('Your roll is:')
    print(dice1)
    print(dice2)
    print(dice3)
    print(dice4)
    print(dice5)
    if dice1 == dice2 == dice3 == dice4 == dice5:
        print('YAHTZEE!!!')
        print("That's an extra 50 points!!!")
    else:
      print('What category would you like to score in? (ones, twos, threes, fours, fives, or sixes)')
      scoring = input()
      sumones = 0 
      sumtwos = 0
      sumthrees = 0
      sumfours = 0
    sumfives = 0
    sumsixes = 0
    sumyh = 0
    if scoring == "ones":
      if dice1 == 1:
        score += 1
      if dice2 == 1: 
        score += 1
      if dice3 == 1: 
        score += 1
      if dice4 == 1: 
        score += 1
      if dice5 == 1:
        score += 1
    elif scoring == "twos":
      if dice1 == 2:
        score += 2
      if dice2 == 2: 
        score += 2
      if dice3 == 2: 
        score += 2
      if dice4 == 2: 
        score += 2
      if dice5 == 2:
        score += 2
    elif scoring == "threes":
      if dice1 == 3:
        score += 3
      if dice2 == 3: 
        score += 3
      if dice3 == 3: 
        score += 3
      if dice4 == 3: 
        score += 3
      if dice5 == 3:
        score += 3
    elif scoring == "fours":
      if dice1 == 4:
        score += 4
      if dice2 == 4: 
        score += 4
      if dice3 == 4: 
        score += 4
      if dice4 == 4: 
        score += 4
      if dice5 == 4:
        score += 4            
    elif scoring == "fives":
      if dice1 == 5:
        score += 5
      if dice2 == 5: 
        score += 5
      if dice3 == 5: 
        score += 5
      if dice4 == 5: 
        score += 5
      if dice5 == 5:
        score += 5                     
    elif scoring == "sixes":
      if dice1 == 6:
        score += 6
      if dice2 == 6: 
        score += 6
      if dice3 == 6: 
        score += 6
      if dice4 == 6: 
        score += 6
      if dice5 == 6:
        score += 6
      





#main program
rollcountvar = 10
rollcount = 1
print('Dice Game')
print("Type 1 to learn to play, and 2 to play")
play = int(input())
if play == 1: #calls learn to play if 1 is typed
  print("Learn To Play") #learn to play section
  print('This game is a version of Yahtzee! the dice game')
  print('The computer will give you commands to type in. It will only work when asked for. To enter a command, type the command then hit enter or return.')
  print('The computer will track your score for you, and it will tell you the rolls you have left after every roll.')
  print('The computer will also total your score for you.')
  print("You get 10 rolls to get the highest score you can. Try to beat your friend's score if taking turns!")
  input('Press enter to play')
  while rollcount <= 10:
    roll()
    print('You have')
    print(rollcountvar - rollcount)
    print('rolls left')
    rollcount += 1
  print('Game Finished!')
  print('Your Total Score Is:')
  print(score)
elif play == 2:#calls the roll program if 2 is typed
  while rollcount <= 10:
    roll()
    print('You have')
    print(rollcountvar - rollcount)
    print('rolls left')
    rollcount += 1
  print('Game Finished!')
  print('Your Total Score Is:')
  print(score)



  