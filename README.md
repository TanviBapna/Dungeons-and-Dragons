Dungeons and Dragons, a popular roleplaying game. 

Introduction :
One of the main components of the game is the dice roll. This allows for randomization and adds variations to the game. Die sides are denoted by d3, d6, d20, etc., with the number referring to the number of sides that the die has. Since we are using a computer, we can have a die like d1000 (meaning a 1000-sided die) which would not be possible in real life. We can also roll multiple dice. 

For example, 1d6 means a six-sided die that can output anything from 1, 2, 3, 4, 5, or 6. 
2d6 means two six-sided dice that can output the sum of two dice throws (e.g., 2 through 12). If the first roll is 3 and the second roll is 2, the sum is 5. 


Each enemy in its own dictionary
There are four enemies total. Each is stored in its own dictionary with key:value pairs for name, attack roll, defense roll, maximum hit points (HP), and current HP. Current HP is like the health of a character. 
A LIST of DICTIONARIES for enemies
The four enemy dictionaries are stored in a list. Meaning, you will have to first get a position in the list, which returns a dictionary, then use that dictionary to find the enemy’s attributes. 
A player dictionary
A player has been created by default. You will enter the player’s name when the program runs. 


Function:
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

Sample : 1
On the next page is sample output showing the information printed by this function. Remember that a vampire starts with 50 HP.

What is the player name: Scotty Highlander
Scotty Highlander currently has 200 hp

1 : Go to Battle
2 : Heal
What to do next > 1
Scotty Highlander encounters a random vampire. Battle starts
Scotty Highlander does 6 damage to vampire
vampire does 0 damage to Scotty Highlander
Scotty Highlander hp: 200
vampire hp: 44
Scotty Highlander does 0 damage to vampire
vampire does 1 damage to Scotty Highlander
Scotty Highlander hp: 199
vampire hp: 44
Scotty Highlander does 7 damage to vampire
vampire does 1 damage to Scotty Highlander
Scotty Highlander hp: 198
vampire hp: 37
Scotty Highlander does 5 damage to vampire
vampire does 1 damage to Scotty Highlander
Scotty Highlander hp: 197
vampire hp: 32
Scotty Highlander does 8 damage to vampire
vampire does 2 damage to Scotty Highlander
Scotty Highlander hp: 195
vampire hp: 24
Scotty Highlander does 3 damage to vampire
vampire does 0 damage to Scotty Highlander
Scotty Highlander hp: 195
vampire hp: 21
Scotty Highlander does 2 damage to vampire
vampire does 3 damage to Scotty Highlander
Scotty Highlander hp: 192
vampire hp: 19
Scotty Highlander does 4 damage to vampire
vampire does 2 damage to Scotty Highlander
Scotty Highlander hp: 190
vampire hp: 15
Scotty Highlander does 0 damage to vampire
vampire does 2 damage to Scotty Highlander
Scotty Highlander hp: 188
vampire hp: 15
Scotty Highlander does 1 damage to vampire
vampire does 1 damage to Scotty Highlander
Scotty Highlander hp: 187
vampire hp: 14
Scotty Highlander does 2 damage to vampire
vampire does 3 damage to Scotty Highlander
Scotty Highlander hp: 184
vampire hp: 12
Scotty Highlander does 5 damage to vampire
vampire does 2 damage to Scotty Highlander
Scotty Highlander hp: 182
vampire hp: 7
Scotty Highlander does 5 damage to vampire
vampire does 1 damage to Scotty Highlander
Scotty Highlander hp: 181
vampire hp: 2
Scotty Highlander does 5 damage to vampire
The vampire has died, hurray!
Press enter to return home

Sample 2:
Here is sample output, continuing from the game above (killing the vampire) which demonstrates the player being healed. 

The vampire has died, hurray!
Press enter to return home
Scotty Highlander currently has 181 hp

1 : Go to Battle
2 : Heal
What to do next > 2
The player takes rest under a healing fountain. Hp restored!
Press any key to return home
Scotty Highlander currently has 200 hp

1 : Go to Battle
2 : Heal
What to do next > 

Sample 3:
Here is sample output, again continuing from the game above, showing that the player has lost a battle (and the game ends). Remember that the battle loop runs until either the player or enemy dies. Sometimes this could take a while because the dice rolls are random. 

Press enter to return home
Scotty Highlander currently has 200 hp

1 : Go to Battle
2 : Heal
What to do next > 1
Scotty Highlander encounters a random dracula. Battle starts
Scotty Highlander does 3 damage to dracula
dracula does 3 damage to Scotty Highlander
Scotty Highlander hp: 197
dracula hp: 197
Scotty Highlander does 2 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 193
dracula hp: 195
Scotty Highlander does 0 damage to dracula
dracula does 6 damage to Scotty Highlander
Scotty Highlander hp: 187
dracula hp: 195
Scotty Highlander does 0 damage to dracula
dracula does 3 damage to Scotty Highlander
Scotty Highlander hp: 184
dracula hp: 195
Scotty Highlander does 0 damage to dracula
dracula does 7 damage to Scotty Highlander
Scotty Highlander hp: 177
dracula hp: 195
Scotty Highlander does 0 damage to dracula
dracula does 2 damage to Scotty Highlander
Scotty Highlander hp: 175
dracula hp: 195
Scotty Highlander does 7 damage to dracula
dracula does 2 damage to Scotty Highlander
Scotty Highlander hp: 173
dracula hp: 188
Scotty Highlander does 4 damage to dracula
dracula does 5 damage to Scotty Highlander
Scotty Highlander hp: 168
dracula hp: 184
Scotty Highlander does 3 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 164
dracula hp: 181
Scotty Highlander does 7 damage to dracula
dracula does 5 damage to Scotty Highlander
Scotty Highlander hp: 159
dracula hp: 174
Scotty Highlander does 5 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 155
dracula hp: 169
Scotty Highlander does 5 damage to dracula
dracula does 5 damage to Scotty Highlander
Scotty Highlander hp: 150
dracula hp: 164
Scotty Highlander does 3 damage to dracula
dracula does 6 damage to Scotty Highlander
Scotty Highlander hp: 144
dracula hp: 161
Scotty Highlander does 0 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 140
dracula hp: 161
Scotty Highlander does 6 damage to dracula
dracula does 1 damage to Scotty Highlander
Scotty Highlander hp: 139
dracula hp: 155
Scotty Highlander does 3 damage to dracula
dracula does 0 damage to Scotty Highlander
Scotty Highlander hp: 139
dracula hp: 152
Scotty Highlander does 6 damage to dracula
dracula does 7 damage to Scotty Highlander
Scotty Highlander hp: 132
dracula hp: 146
Scotty Highlander does 6 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 128
dracula hp: 140
Scotty Highlander does 3 damage to dracula
dracula does 7 damage to Scotty Highlander
Scotty Highlander hp: 121
dracula hp: 137
Scotty Highlander does 2 damage to dracula
dracula does 8 damage to Scotty Highlander
Scotty Highlander hp: 113
dracula hp: 135
Scotty Highlander does 4 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 109
dracula hp: 131
Scotty Highlander does 0 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 105
dracula hp: 131
Scotty Highlander does 6 damage to dracula
dracula does 8 damage to Scotty Highlander
Scotty Highlander hp: 97
dracula hp: 125
Scotty Highlander does 6 damage to dracula
dracula does 2 damage to Scotty Highlander
Scotty Highlander hp: 95
dracula hp: 119
Scotty Highlander does 2 damage to dracula
dracula does 3 damage to Scotty Highlander
Scotty Highlander hp: 92
dracula hp: 117
Scotty Highlander does 5 damage to dracula
dracula does 3 damage to Scotty Highlander
Scotty Highlander hp: 89
dracula hp: 112
Scotty Highlander does 7 damage to dracula
dracula does 1 damage to Scotty Highlander
Scotty Highlander hp: 88
dracula hp: 105
Scotty Highlander does 0 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 84
dracula hp: 105
Scotty Highlander does 4 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 80
dracula hp: 101
Scotty Highlander does 4 damage to dracula
dracula does 3 damage to Scotty Highlander
Scotty Highlander hp: 77
dracula hp: 97
Scotty Highlander does 2 damage to dracula
dracula does 0 damage to Scotty Highlander
Scotty Highlander hp: 77
dracula hp: 95
Scotty Highlander does 2 damage to dracula
dracula does 8 damage to Scotty Highlander
Scotty Highlander hp: 69
dracula hp: 93
Scotty Highlander does 7 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 65
dracula hp: 86
Scotty Highlander does 3 damage to dracula
dracula does 2 damage to Scotty Highlander
Scotty Highlander hp: 63
dracula hp: 83
Scotty Highlander does 3 damage to dracula
dracula does 5 damage to Scotty Highlander
Scotty Highlander hp: 58
dracula hp: 80
Scotty Highlander does 0 damage to dracula
dracula does 2 damage to Scotty Highlander
Scotty Highlander hp: 56
dracula hp: 80
Scotty Highlander does 0 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 52
dracula hp: 80
Scotty Highlander does 1 damage to dracula
dracula does 5 damage to Scotty Highlander
Scotty Highlander hp: 47
dracula hp: 79
Scotty Highlander does 2 damage to dracula
dracula does 5 damage to Scotty Highlander
Scotty Highlander hp: 42
dracula hp: 77
Scotty Highlander does 4 damage to dracula
dracula does 1 damage to Scotty Highlander
Scotty Highlander hp: 41
dracula hp: 73
Scotty Highlander does 1 damage to dracula
dracula does 8 damage to Scotty Highlander
Scotty Highlander hp: 33
dracula hp: 72
Scotty Highlander does 7 damage to dracula
dracula does 6 damage to Scotty Highlander
Scotty Highlander hp: 27
dracula hp: 65
Scotty Highlander does 3 damage to dracula
dracula does 7 damage to Scotty Highlander
Scotty Highlander hp: 20
dracula hp: 62
Scotty Highlander does 4 damage to dracula
dracula does 7 damage to Scotty Highlander
Scotty Highlander hp: 13
dracula hp: 58
Scotty Highlander does 4 damage to dracula
dracula does 7 damage to Scotty Highlander
Scotty Highlander hp: 6
dracula hp: 54
Scotty Highlander does 5 damage to dracula
dracula does 4 damage to Scotty Highlander
Scotty Highlander hp: 2
dracula hp: 49
Scotty Highlander does 5 damage to dracula
dracula does 6 damage to Scotty Highlander
Oh no! Scotty Highlander
Player is dead!
How the game ends
The game runs infinitely as long as the player is alive. Remember that when an enemy dies, their HP is reset to their maximum, so there could theoretically be infinite battles. 

The game ends when the player dies. 