import random

# Enemies defined in different dictionaries
vampire = {"name": "Vampire", "attack":"1d5", "defense": "1d3", "maxhp":50, "curhp":50 }
goblin = {"name": "Goblin", "attack":"1d3", "defense": "1d1", "maxhp":30, "curhp":30 }
ghost = {"name": "Ghost", "attack":"1d5", "defense": "1d5", "maxhp":50, "curhp":50 }
dracula = {"name": "Dracula", "attack":"2d5", "defense": "1d4", "maxhp":200, "curhp":200 }

# A LIST of DICTIONARIES for enemies
enemies = [vampire, goblin, ghost, dracula]

# Player dictionary
player = {"name":"", "attack":"2d5", "defense": "1d3", "maxhp":200, "curhp":200}

def do_battle(player, enemy):
    # This function calls get_damage() twice, once for player and once for enemy
    
    flag = "true"
    while(flag == "true"):
        
        # Damage done by Player
        player_attack = get_damage(player['attack'],enemy['attack'])
        print(player['name']," does ",player_attack," damage to ",enemy['name'])
    
        #Damage done by enemy
        enemy_attack = get_damage(enemy['attack'],player['attack'])
        print(enemy['name']," does ",enemy_attack," damage to ",player['name'])
        
        # Calculating their current hps
        player['curhp'] = player['curhp'] - enemy_attack
        enemy['curhp'] = enemy['curhp'] - player_attack
        
        print(player['name']," hp:",player['curhp'])
        print(enemy['name']," hp:",enemy['curhp'])
        
        if (player['curhp'] <= 0):
            flag = "false"
            return False 
        elif(enemy['curhp'] <=0):
            flag = "false"
            return True
        
    return False
    
def get_damage(attack, defense):
    # This function calls get_roll() twice, once for the attack roll and once for the defense roll
    
    # Attack Hp
    attack_roll = get_roll(attack)
    
    # Defense Hp
    defense_roll = get_roll(defense)
    
    if defense_roll> attack_roll:
        return 0 
    else:
        return attack_roll - defense_roll
        
def get_roll(rollstring):
    # Splitting the string to get number of dices and number of sides
    num = rollstring.split("d")
    total = 0
    
    # Loop for number of Dices
    for i in range(0, int(num[0])):
        # Generating a random integer between 1 and number of sides and adding to create a total
        total = total+ random.randint(1,int(num[1]))
    return total


def main_menu_goto_battle():
    enemy = enemies[random.randint(0,len(enemies)-1)]
    if do_battle(player, enemy):
        print(f"The {enemy['name']} has died, hurray!")
        enemy['curhp'] = enemy['maxhp']
        input("Press enter to return home")
    else:
        print(f"Oh no! {player['name']}")

    return


def main_menu_heal():
    print(f"The player takes rest under a healing fountain. HP restored!")
    player['curhp'] = player['maxhp']
    input("Press enter to return home")
    return


def main_menu():
    # Player dies if player HP reaches 0 or less
    while player['curhp'] > 0:
        # Display menu
        print(f"{player['name']} currently has {player['curhp']} hp\n")
        print("1 : Go to Battle")
        print("2 : Heal")

        x = input("What to do next > ")
        # Get input from player
        if x =="1":
            main_menu_goto_battle()
        elif x=="2":
            main_menu_heal()
        else:
            print("No such action")

    print("Player is dead!")

player['name'] = input("What is the player's name? ")
main_menu()


