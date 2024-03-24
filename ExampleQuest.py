# ExampleQuest - a turn based battle
'''

- displayIntro(): Display an intro
---print title
---ask user if they want instructions
---ask if they want to see the story

-createCharacter(): Create a character
gives the option of 2 characters with different stats and special abilities
charInfo = [name, type/character class, HP, attack, speed]
name - string with character name - user entered
type/character class - type of character
HP - int, how much health they have
attack - int, random range, based on character type
speed - int, represents chance to dodge attack
special - int, how many times special can be used

-createEnemy(): Create an enemy
enemyInfo = [name, type/character class, HP, attack, speed]
name - string with character name
type/character class - type of character
HP - int, how much health they have
attack - int, random range, based on character type
speed - int, represents chance to dodge attack

-fight(player, enemy): --> result (string)
announce fight
while no one is dead (HP > 0):
    get player attack option
        attack - generate damage int based on attack, reduce enemys HP by that amt
        flee - roll a die, if we beat some number, we escape
        special - special action for each character type
    get enemy attack option
        attack -generate damage int based on attack, reduce players HP by that amt
        special - special action for each character type
return "player" if player wins, "flee" if player flees, else return "enemy"

-ending(result): Print ending
if player is alive print good ending
if player is dead print bad ending

'''

import random
from PrintTools import sPrint
import ASCIIArt


NAME = 0
TYPE = 1
HP = 2
ATK = 3
SPD = 4
SPECIAL = 5

def displayIntro():
    ASCIIArt.title_art()
    story = """
        Long ago your great-grandmother set off on a quest to protect her village. 
        Her goal was to reach the top of Scarworth Mountain and return with a Daedra heart 
        but she was captured along the way, never to be seen again. Now it is up to you to 
        seek vengeance and restore a name for your village!
             """
    rules = """
        Choose your fighter. Begin your ascent up Scarworth Mountain. Once you encounter an enemy, 
        you will take turns dealing damage and fight to the death. On your turn, choose 
        whether you will fight or flee. Only one shall survive!
    """

    choice = input("View the story? (y/n): ")
    if choice.lower() == "y":
        sPrint(story)
    choice = input("View the rules? (y/n): ")
    if choice.lower() == "y":
        sPrint(rules, 0.06)

def createCharacter():
    player = ["", "", 0, 0, 0, 0]
    characterMenu = '''
            CHARACTER OPTIONS:

            CHARACTER 1
            ------------
            Type - Assassin
            HP - 100
            SPD - 15
            Special - Shield Bash - Increases damage and reduces your enemy's speed.

            CHARACTER 2
            ------------
            Type - Necromancer
            HP - 100
            SPD - 10
            Special - Health Potion - adds 10 HP. 

            Pick your fighter (1 or 2)
        '''
    print(characterMenu)
    choice = input(">>> ")
    while choice not in ("1", "2"):
        print("Please make a valid selection.")
        choice = input(">>> ")
    if choice == "1":
        player[NAME] = input("Enter your name, warrior: ")
        player[TYPE] = "Assassin"
        player[HP] = 100
        player[ATK] = random.randint(10, 20)
        player[SPD] = 15
        player[SPECIAL] = 2
        return player
    elif choice == "2":
        player = ["", "", 0, 0, 0, 0]
        player[NAME] = input("Enter your name, warrior: ")
        player[TYPE] = "Necromancer"
        player[HP] = 100
        player[ATK] = random.randint(10, 20)
        player[SPD] = 10
        player[SPECIAL] = 2
        return player


def createEnemy():
    enemy = ["", "", 0, 0, 0, 0]
    enemyNames = ["Scorpion", "Nemesis", "Valkyrie Queen", "Draugr Lord", "Corpse Eater", "Huntress"]
    enemyTypes = ["Demon", "Troll", "Dark Elf", "Mage", "Cyborg", "Unknown"]
    enemy[NAME] = random.choice(enemyNames)
    enemy[TYPE] = random.choice(enemyTypes)
    enemy[HP] = random.randint(60, 100)
    enemy[ATK] = random.randint(10, 20)
    enemy[SPD] = random.randint(5, 20)
    enemy[SPECIAL] = 3
    return enemy

def fight(player, enemy):
    fled = False
    isPoisoned = False
    poisonedTurns = 0
    poisonPerGame = True
    menu = '''
    A) ATTACK
    B) FLEE
    C) SPECIAL
    '''
    sPrint(f"A wild {enemy[TYPE]} approaches!")
    enemy_image = ASCIIArt.enemy_art(enemy=enemy[TYPE])  #ASCII art for randomly generated enemy
    print(enemy_image)
    sPrint("FIGHT    OR    DIE!")
    while player[HP] > 0 and enemy[HP] > 0 and not fled:
        print("\n===================")
        print(f"{enemy[NAME]} HP: {enemy[HP]}")
        print(f"{player[NAME]} HP: {player[HP]}")
        print("===================")

        #####PLAYER TURN####
        print(menu)
        choice = input(">>> ").lower()
        while choice not in ("a", "b", "c"):
            choice = input(">>>")
        if player[HP] <= 20 and enemy[HP] >= 30:
            player[HP] += 8
            sPrint(f"Health boost! Your HP is now {player[HP]}.")
        if choice == "a":
            #print attack message
            sPrint(f"You swing at {enemy[NAME]}, the {enemy[TYPE]} ")
            #check if we hit enemy - roll b/t 100. if the roll is greater than their SPD, we hit
            roll = random.randint(1, 100)
            if roll > enemy[SPD]:
                sPrint(f"...land a solid hit and deal {player[ATK]} damage!", 0.06)
                enemy[HP] -= player[ATK]
            else:
                sPrint("...but you miss!")
        elif choice == "b": #flee attempt
            sPrint("The battle is hopeless...you must escape!")
            roll = random.randint(1, 100)
            if roll > player[SPD] + 10:
                fled = True
        elif choice == "c": #special attack
            if player[TYPE] == "Assassin":
                if player[SPECIAL] > 0:
                    originalATK = player[ATK]
                    player[ATK] += 5
                    enemy[SPD] /= 2
                    enemy[HP] -= player[ATK]
                    player[SPECIAL] -= 1
                    sPrint(f"Shield Bash! Your deal {player[ATK]} damage and {enemy[NAME]}'s SPD is now {enemy[SPD]}.")
                    player[ATK] = originalATK #returns player[ATK] to original value

                else:
                    print("Sorry, you've run out of special attacks.")
            if player[TYPE] == "Necromancer":
                if player[SPECIAL] > 0:
                    player[HP] += 10
                    player[SPECIAL] -= 1
                    sPrint(f"Health Potion! Your HP has increased by 10 and is now {player[HP]}.")
                else:
                    print("Sorry, you've run out of special attacks.")

        ###ENEMY TURN###
        if enemy[HP] > 0:
            sPrint(f"{enemy[NAME]} lashes out at you!")
            roll = random.randint(1, 100)
            if roll > player[SPD]:
                sPrint(f"...you've been hit! You've taken {enemy[ATK]} damage!", 0.06)
                player[HP] -= enemy[ATK]
            else:
                print(f"Cat-like reflexes, {player[NAME]}! You dodged {enemy[NAME]}'s hit!")
        if poisonPerGame:
            another_roll = random.randint(1, 10)
            #print(f"another roll: {another_roll}") #breakpt for debugging
            if another_roll in range(3, 6):
                #if another_roll is b/t 3-6, the poison effect begins
                isPoisoned = True
                poisonedTurns = 3 #player is poisoned for 3 turns
                poisonPerGame = False #can only use poison one time per game

        if isPoisoned: #during the 3 poisoned turns in a row
            player[HP] -= 3 #decrases players health by a small amt
            poisonedTurns -= 1 #subtracts 1 per turn so poison effect only lasts 3 turns
            sPrint(f"{enemy[NAME]} has poisoned you! Your health is slowly declining!")
            if poisonedTurns == 0: #once the 3 poisoned turns run out, the poison effect turns off
                isPoisoned = False



    if fled:
        return "fled"
    elif player[HP] <= 0:
        return "enemy"
    elif enemy[HP] <=0:
        return "player"


def ending(result):
    if result == "player":
        print("\nYou have avenged your great-grandmother and restored honor to your village! "
              "Victory is yours!")
    elif result == "enemy":
        print("\nLosing must run in the family...")
    else:
        print(f"\nYou managed to escape the attack...coward!")

def main():
    displayIntro()
    player = createCharacter()
    enemy = createEnemy()
    result = fight(player, enemy)
    ending(result)

main()