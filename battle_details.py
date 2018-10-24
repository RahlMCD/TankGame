import random

from tank_specifications import *


# This will select which tank fires first
def coin_flip():
    panzer_tank = 1
    flip = random.randint(1,2)
    if flip == panzer_tank:
        first_to_shoot = "Panzer"
    else:
        first_to_shoot = "T34"
    return  first_to_shoot


def shot(receiver, damage):
    receiver = receiver - damage
    return receiver


def target_choice(armor):
    x = random.randint(0,3)
    while armor[x] > 0 :
        target_armor = armor[x]
        return target_armor


def hit_chance(author, receiver):
    percentage_chance = random.randint(0,100)
    print(author+ " " + "has" + " " + str(percentage_chance) + "% chances to hit" + " " + receiver)
    if random.randint(0,100) < percentage_chance:
        return True
    else:
        return False


def round():

    if coin_flip() == "Panzer":
        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            try:
                item_hit_1st = target_choice(t34_defensive_stats)
                item_hit_1st -= panzer_damage[0]
                print("T34 tank was hit")
            except Exception as e:
                print('T34 tank has been defeated')
        else:
            print("MISS")
        author = "T34"
        receiver = 'Panzer'
        if hit_chance(author, receiver) is True:
            item_hit_2nd = target_choice(panzer_defensive_stats)
            item_hit_2nd -= t34_damage[0]
            print("Panzer tank was hit")
        else:
            print("Miss")
    elif coin_flip() == "T34:":
        author = "T34"
        receiver = 'Panzer'
        if hit_chance(author, receiver) is True:
            item_hit_1st = target_choice(panzer_defensive_stats)
            item_hit_1st -= t34_damage[0]
            print("Panzer tank was hit")
        else:
            print("MISS")
        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            item_hit_2nd = target_choice(t34_defensive_stats)
            item_hit_2nd -= panzer_damage[0]
            print("T34 tank was hit")
        else:
            print("Miss")




