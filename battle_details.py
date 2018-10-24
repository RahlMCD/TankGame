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


def fire(target, damage):
    target -= damage
    return  target


def hit_chance():
    percentage_chance = random.randint(0,100)
    print("You have" + " " + str(percentage_chance) + "% chances to get it right.")
    if random.randint(0,100) < percentage_chance:
        return True
    else:
        return False



round()
