# Dungeons and Dragons, a popular roleplaying game. 

## Introduction :
One of the main components of the game is the dice roll. This allows for randomization and adds variations to the game. Die sides are denoted by d3, d6, d20, etc., with the number referring to the number of sides that the die has. Since we are using a computer, we can have a die like d1000 (meaning a 1000-sided die) which would not be possible in real life. We can also roll multiple dice. 

For example, 1d6 means a six-sided die that can output anything from 1, 2, 3, 4, 5, or 6. 
2d6 means two six-sided dice that can output the sum of two dice throws (e.g., 2 through 12). If the first roll is 3 and the second roll is 2, the sum is 5. 


## Each enemy in its own dictionary.
There are four enemies total. Each is stored in its own dictionary with key:value pairs for name, attack roll, defense roll, maximum hit points (HP), and current HP. Current HP is like the health of a character. 

## A LIST of DICTIONARIES for enemies:
The four enemy dictionaries are stored in a list. Meaning, you will have to first get a position in the list, which returns a dictionary, then use that dictionary to find the enemy’s attributes. 

## A player dictionary:
A player has been created by default. You will enter the player’s name when the program runs. 


## Function:
get_roll(rollstring) :
This function takes an input parameter as a string that looks like “1d3”, “3d5”, etc. The function should return an integer simulating those dice rolls. In the case of “3d5”, for example, the function will generate a random number between 1 and 5, three times, and return the total as an integer. 

get_damage(attack, defense) :
This function gets the value of damage based on roll strings. If the defense roll is greater than the attack roll, damage is 0. Otherwise, return attack minus defense, as an integer. 

do_battle(player, enemy) :
This is the main battle function. Notice that it is called from main_menu_goto_battle(). In this function, a loop runs until either the player or enemy is dead. For each battle round, display the damage done by the player (to the enemy), the damage done by the enemy (to the player), and the new HP for the player and enemy after those damages are deducted. If the enemy dies, return True. If the player dies, return False. 

main_menu_goto_battle() :
This function chooses a random enemy for the player to battle. The output is either the enemy dies or the player dies. If the enemy dies, their current HP is reset to their maximum HP.

main_menu_heal() :
This function restores the player’s current HP to their maximum HP. 

main_menu() :
This is the main menu of the game where the user can choose what action (battle or heal) they would like to do. The main menu appears as long as the player’s HP is above 0. Once it gets below 0, meaning the player has died, the program notifies the user and the game ends. 
