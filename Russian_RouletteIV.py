# GameVault - A Treasure Trove of Minigames  
# Featuring classics like Russian Roulette, Blackjack, and JoJo-inspired adventures!  
# Created with passion by Neel (@NotNxel)  
# Explore more: https://github.com/NotNxel/GameVault  
# © 2025 Neel And Reyansh. All rights reserved.  

#importing modules

import random

#Player Names

global Player1

Player1 = input('What is the name of player 1? : ')
print('\n')

global Player2

Player2 = input('What is the name of player 2? : ')
print('\n')

print('Welcome to Russian Roulette, ' + Player1 + ' and ' + Player2 + '\n')

#CHANGE_RULES Later

#Rules

print(
    'The rules are simple, ' + Player1 + ' and ' + Player2 +
    ' will take turns shooting each other. If you shoot yourself, you lose a life. ' +
    'If you shoot the other player, he loses a life. ')

print('\n')

print(
    'There are 5 abilities.'+ '\n \n' +
    'Magnifying Glass: If used, tells whether the current shot is BLANK or LIVE. \n' +
    'Knife: If used, changes the gun into a shotgun, which deals 2 hearts of damage instead of 1. \n'+
    'Medicine: If used, heals 1 heart. \n'+
    'Coca-cola: Ejects the current shot in the barrel, regardless of whether it is blank or live. \n')


#Design (Game Intro)

print('=============================================')
print('               RUSSIAN ROULETTE              ')
print('=============================================')

print('\n')

#Random Turn
players = [Player1, Player2]

global Turn
Turn = random.choice(players)

global new_turn
new_turn = ""

global Player1Heart
Player1Heart = 5

global Player2Heart
Player2Heart = 5

global Player1Abilities
Player1Abilities = []

global Player2Abilities
Player2Abilities = []


def abilities_func():

  abilities = ["Magnifying Glass", "Knife", "Coca-Cola", "Medicine", "Handcuffs"]

  for _ in range(4 - len(Player1Abilities)):
    ability1 = random.choice(abilities)

    Player1Abilities.append(ability1)

  for _ in range(4 - len(Player2Abilities)):
    ability2 = random.choice(abilities)

    Player2Abilities.append(ability2)

  player1_ab = ''

  global a1
  a1 = 0
  for elm in Player1Abilities:
    a1 += 1
    if a1 == 4:
      player1_ab += elm
    else:
      player1_ab += elm + ', ' 


  player2_ab = ''

  global a2
  a2 = 0
  for elm in Player2Abilities:
    a2 += 1
    if a2 == 4:
      player2_ab += elm
    else:
      player2_ab += elm + ', '

  print('These are', Player1 + '\'s Abilities :', player1_ab, '\n')
  print('These are', Player2 + '\'s Abilities :', player2_ab, '\n')


print("There Are 8 Shots")

print(Player1 + " has " + str(Player1Heart) + " lives")

print(Player2 + " has " + str(Player2Heart) + " lives")

#Defining Barrel

global barrel
barrel = []


def barrel_func():

  LIVE = random.randint(3, 6)
  BLANK = (8 - LIVE)

  print("=============================================")
  print("Live Shots = " + str(LIVE))
  print("Blank Shots = " + str(BLANK))
  print("=============================================")

  for _ in range(LIVE):
    barrel.append('LIVE')
  for _ in range(BLANK):

    barrel.append('BLANK')
  random.shuffle(barrel)


#Defining Choice and Shooting And all


def shoot():

  global Player1Heart
  global Player2Heart
  global new_turn

  global Turn

  if Player1Heart == 0:
    print(Player2, 'Wins!')

  elif Player2Heart == 0:
    print(Player1, 'Wins!')

  if new_turn == Player1:
    Turn = Player1

  elif new_turn == Player2:
    Turn = Player2

  elif barrel == []:
    barrel_func()
    abilities_func()

  print("It is " + Turn + "'s turn.\n")

  #Defining Abilities

  global shotgunplayer2
  shotgunplayer2 = 0

  global shotgunplayer1
  shotgunplayer1 = 0

  def magnifying_glass():
    print("The barrel has a", barrel[0], "shot for this turn.")

  def knife():

    global shotgunplayer1
    shotgunplayer1 = 0

    global shotgunplayer2
    shotgunplayer2 = 0

    if Turn == Player1:
      shotgunplayer1 += 1

    elif Turn == Player2:
      shotgunplayer2 += 1

  def Coca_Cola():
    print('It was a ', barrel[0], 'Shot')
    barrel.pop(0)

  def medicine():
    global Player1Heart
    global Player2Heart

    if Turn == Player1:
      Player1Heart += 1

    elif Turn == Player2:
      Player2Heart += 1

  def Handcuffs():
    new_turn = ""

    global Turn

    if Turn == Player1:
      new_turn = Player1

    if Turn == Player2:
      new_turn = Player2

  choice = input(
      "Press 1 if you want to shoot , or 2 if you want to use ability : ")

  if choice == '1':
    shootchoice = input("Choose 1 for Shooting " + Player1 +
                        " or 2 for Shooting " + Player2 + ': ')

    if Turn == Player1 and shootchoice == '1':
      if barrel[0] == 'LIVE':
        if shotgunplayer1 == 0:
          print(Player1 + " Shoots Himself")
          Player1Heart = Player1Heart - 1
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          barrel.pop(0)
          Turn = Player2
          shotgunplayer1 = 0
          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          print("=============================================")
          shoot()
        elif shotgunplayer1 == 1:
          print(Player1 + " Shoots Himself")
          Player1Heart = Player1Heart - 2
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          print("=============================================")
          barrel.pop(0)
          Turn = Player2
          shotgunplayer1 = 0
          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer1 == 0:
        print(Player1 + " Shoots Himself")
        Player1Heart = Player1Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        shotgunplayer1 = 0
        Turn = Player1
        if new_turn != "":
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer1 == 1:
        print(Player1 + "Shoots Himself")
        Player1Heart = Player1Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        shotgunplayer1 = 0
        Turn = Player1

        if new_turn != "":
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
    if Turn == Player1 and shootchoice == '2':
      if barrel[0] == 'LIVE':
        if shotgunplayer1 == 0:
          print(Player1 + " Shoots " + Player2)
          Player2Heart = Player2Heart - 1
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          barrel.pop(0)
          Turn = Player2

          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          print("=============================================")
          shoot()
        elif shotgunplayer1 == 1:
          print(Player1 + " Shoots " + Player2)
          Player2Heart = Player2Heart - 2
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          print("=============================================")
          barrel.pop(0)
          shotgunplayer1 = 0
          Turn = Player2
          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer1 == 0:
        print(Player1 + " Shoots " + Player2)
        Player2Heart = Player2Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        shotgunplayer1 = 0
        Turn = Player2
        if new_turn != "":
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer1 == 1:
        print(Player1 + " Shoots " + Player2)
        Player1Heart = Player1Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        shotgun = 0
        shotgunplayer1 = 0
        Turn = Player2
        if new_turn != '':
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
    elif Turn == Player2 and shootchoice == '2':
      if barrel[0] == 'LIVE':
        if shotgunplayer2 == 0:
          print(Player2 + " Shoots Himself")
          Player2Heart = Player2Heart - 1
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          barrel.pop(0)
          shotgunplayer2 = 0
          Turn = Player1
          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          print("=============================================")
          shoot()
        elif shotgunplayer2 == 1:
          print(Player2 + " Shoots Himself")
          Player2Heart = Player2Heart - 2
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          print("=============================================")
          barrel.pop(0)
          Turn = Player1
          shotgunplayer2 = 0
          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer2 == 0:
        print(Player2 + " Shoots Himself")
        Player2Heart = Player2Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        Turn = Player2
        shotgunplayer2 = 0
        if new_turn != "":
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer2 == 1:
        print(Player2 + " Shoots Himself")
        Player2Heart = Player2Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        shotgun = 0
        Turn = Player2
        shotgunplayer2 = 0
        if new_turn != "":
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
    elif Turn == Player2 and shootchoice == '1':
      if barrel[0] == 'LIVE':
        if shotgunplayer2 == 0:
          print(Player2 + " Shoots " + Player1)
          Player1Heart = Player1Heart - 1
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          barrel.pop(0)
          shotgunplayer2 = 0
          Turn = Player1
          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          print("=============================================")
          shoot()
        elif shotgunplayer2 == 1:
          print(Player2 + " Shoots " + Player1)
          Player1Heart = Player1Heart - 2
          print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
          print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
          print("=============================================")
          barrel.pop(0)
          Turn = Player1
          shotgunplayer2 = 0
          if new_turn != "":
            Turn = new_turn
          new_turn = ""
          shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer2 == 0:
        print(Player2 + " Shoots " + Player1)
        Player1Heart = Player1Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        Turn = Player1
        shotgunplayer2 = 0
        if new_turn != "":
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
      elif barrel[0] == 'BLANK' and shotgunplayer2 == 1:
        print(Player2 + " Shoots " + Player1)
        Player1Heart = Player1Heart - 0
        print(Player1 + " Has " + str(Player1Heart) + " Lives Left")
        print(Player2 + " Has " + str(Player2Heart) + " Lives Left")
        barrel.pop(0)
        shotgun = 0
        shotgunplayer2 = 0
        Turn = Player1
        if new_turn != "":
          Turn = new_turn
        new_turn = ""
        print("=============================================")
        shoot()
  elif choice == '2':

    if Turn == Player1:
      global ability_choice
      ability_choice = None
      if len(Player1Abilities) == 4:
        ability_choice = input("Press 1 for " + Player1Abilities[0] +
                               " or 2 for " + Player1Abilities[1] +
                               ' or 3 for ' + Player1Abilities[2] +
                               ' or 4 for ' + Player1Abilities[3] + ' : ')
      elif len(Player1Abilities) == 3:
        ability_choice = input("Press 1 for " + Player1Abilities[0] +
                               " or 2 for " + Player1Abilities[1] +
                               ' or 3 for ' + Player1Abilities[2] + ' : ')
      elif len(Player1Abilities) == 2:
        ability_choice = input("Press 1 for " + Player1Abilities[0] +
                               " or 2 for " + Player1Abilities[1] + ' : ')
      elif len(Player1Abilities) == 1:
        ability_choice = input("Press 1 for " + Player1Abilities[0] + ' : ')
      elif len(Player1Abilities) == 0:
        print("You have no abilities left")
        shoot()

      if ability_choice == '1':
        if Player1Abilities[0] == 'Magnifying Glass':
          magnifying_glass()
          Player1Abilities.pop(0)
          shoot()
        elif Player1Abilities[0] == 'Knife':
          knife()
          Player1Abilities.pop(0)
          shoot()
        elif Player1Abilities[0] == 'Medicine':
          medicine()
          Player1Abilities.pop(0)
          shoot()
        elif Player1Abilities[0] == 'Handcuffs':
          Handcuffs()
          Player1Abilities.pop(0)
          shoot()
        elif Player1Abilities[0] == 'Coca-Cola':
          Coca_Cola()
          Player1Abilities.pop(0)
          shoot()
      elif ability_choice == '2':
        if Player1Abilities[1] == 'Magnifying Glass':
          magnifying_glass()
          Player1Abilities.pop(1)
          shoot()
        elif Player1Abilities[1] == 'Knife':
          knife()
          Player1Abilities.pop(1)
          shoot()
        elif Player1Abilities[1] == 'Medicine':
          medicine()
          Player1Abilities.pop(1)
          shoot()
        elif Player1Abilities[1] == 'Handcuffs':
          Handcuffs()
          Player1Abilities.pop(1)
          shoot()
        elif Player1Abilities[1] == 'Coca-Cola':
          Coca_Cola()
          Player1Abilities.pop(1)
          shoot()
      elif ability_choice == '3':
        if Player1Abilities[2] == 'Magnifying Glass':
          magnifying_glass()
          Player1Abilities.pop(2)
          shoot()
        elif Player1Abilities[2] == 'Knife':
          knife()
          Player1Abilities.pop(2)
          shoot()
        elif Player1Abilities[2] == 'Medicine':
          medicine()
          Player1Abilities.pop(2)
        elif Player1Abilities[2] == 'Handcuffs':
          Handcuffs()
          Player1Abilities.pop(2)
          shoot()
        elif Player1Abilities[2] == 'Coca-Cola':
          Coca_Cola()
          Player1Abilities.pop(2)
          shoot()
      elif ability_choice == '4':
        if Player1Abilities[3] == 'Magnifying Glass':
          magnifying_glass()
          Player1Abilities.pop(3)
          shoot()
        elif Player1Abilities[3] == 'Knife':
          knife()
          Player1Abilities.pop(3)
          shoot()
        elif Player1Abilities[3] == 'Medicine':
          medicine()
          Player1Abilities.pop(3)
          shoot()
        elif Player1Abilities[3] == 'Handcuffs':
          Handcuffs()
          Player1Abilities.pop(3)
        elif Player1Abilities[3] == 'Coca-Cola':
          Coca_Cola()
          Player1Abilities.pop(3)
          shoot()
    elif Turn == Player2:
      ability_choice = None
      if len(Player2Abilities) == 4:
        ability_choice = input("Press 1 for " + Player2Abilities[0] +
                               " or 2 for " + Player2Abilities[1] +
                               ' or 3 for ' + Player2Abilities[2] +
                               ' or 4 for ' + Player2Abilities[3] + ' : ')
      elif len(Player2Abilities) == 3:
        ability_choice = input("Press 1 for " + Player2Abilities[0] +
                               " or 2 for " + Player2Abilities[1] +
                               ' or 3 for ' + Player2Abilities[2] + ' : ')
      elif len(Player2Abilities) == 2:
        ability_choice = input("Press 1 for " + Player2Abilities[0] +
                               " or 2 for " + Player2Abilities[1] + ' : ')
      elif len(Player2Abilities) == 1:
        ability_choice = input("Press 1 for " + Player2Abilities[0] + ' : ')
      else:
        print("You have no abilities left")
        shoot()

      if ability_choice == '1':
        if Player2Abilities[0] == 'Magnifying Glass':
          magnifying_glass()
          Player2Abilities.pop(0)
          shoot()
        elif Player2Abilities[0] == 'Knife':
          knife()
          Player2Abilities.pop(0)
          shoot()
        elif Player2Abilities[0] == 'Medicine':
          medicine()
          Player2Abilities.pop(0)
          shoot()
        elif Player2Abilities[0] == 'Handcuffs':
          Handcuffs()
          Player2Abilities.pop(0)
          shoot()
        elif Player2Abilities[0] == 'Coca-Cola':
          Coca_Cola()
          Player2Abilities.pop(0)
          shoot()
      elif ability_choice == '2':
        if Player2Abilities[1] == 'Magnifying Glass':
          magnifying_glass()
          Player2Abilities.pop(1)
          shoot()
        elif Player2Abilities[1] == 'Knife':
          knife()
          Player2Abilities.pop(1)
          shoot()
        elif Player1Abilities[1] == 'Medicine':
          medicine()
          Player2Abilities.pop(1)
          shoot()
        elif Player1Abilities[1] == 'Handcuffs':
          Handcuffs()
          Player2Abilities.pop(1)
          shoot()
        elif Player2Abilities[1] == 'Coca-Cola':
          Coca_Cola()
          Player2Abilities.pop(1)
          shoot()
      elif ability_choice == '3':

        if Player2Abilities[2] == 'Magnifying Glass':
          magnifying_glass()
          Player2Abilities.pop(2)
          shoot()
        elif Player2Abilities[2] == 'Knife':
          knife()
          Player2Abilities.pop(2)
          shoot()
        elif Player2Abilities[2] == 'Medicine':
          medicine()
          Player2Abilities.pop(2)
          shoot()
        elif Player2Abilities[2] == 'Handcuffs':
          Handcuffs()
          Player2Abilities.pop(2)
          shoot()
        elif Player2Abilities[2] == 'Coca-Cola':
          Coca_Cola()
          Player2Abilities.pop(2)
          shoot()

      elif ability_choice == '4':
        if Player2Abilities[3] == 'Magnifying Glass':
          magnifying_glass()
          Player2Abilities.pop(3)
          shoot()
        elif Player2Abilities[3] == 'Knife':
          knife()
          Player2Abilities.pop(3)
          shoot()
        elif Player2Abilities[3] == 'Medicine':
          medicine()
          Player2Abilities.pop(3)
          shoot()
        elif Player2Abilities[3] == 'Handcuffs':
          Handcuffs()
          Player2Abilities.pop(3)
          shoot()
        elif Player2Abilities[3] == 'Coca-Cola':
          Coca_Cola()
          Player2Abilities.pop(3)
          shoot()


barrel_func()
abilities_func()
shoot()
