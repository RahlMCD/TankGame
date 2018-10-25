import random

from tank_specifications import *

panzer_front_armor = panzer_defensive_stats[0]
panzer_left_armor = panzer_defensive_stats[1]
panzer_right_armor = panzer_defensive_stats[2]
panzer_rear_armor = panzer_defensive_stats[3]

t34_front_armor = t34_defensive_stats[0]
t34_left_armor = t34_defensive_stats[1]
t34_right_armor = t34_defensive_stats[2]
t34_rear_armor = t34_defensive_stats[3]

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


def opening_round():
    panzer_end_stats = []
    t34_end_stats = []
    if coin_flip() == "Panzer":
        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            t34_end_front_armor = t34_front_armor - panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(0, t34_end_front_armor)
        else:
            print("MISS")
            t34_end_stats.insert(0,t34_front_armor)
        author = "T34"
        receiver = 'Panzer'
        if hit_chance(author, receiver) is True:
            panzer_end_front_armor = panzer_front_armor - t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(0,panzer_end_front_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(0, panzer_front_armor)

        if hit_chance(author, receiver) is True:
            t34_end_left_armor = t34_left_armor - panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(1,t34_end_left_armor)
        else:
            print("MISS")
            t34_end_stats.insert(1, t34_left_armor)
        author = "T34"
        receiver = 'Panzer'
        if hit_chance(author, receiver) is True:
            panzer_end_left_armor = panzer_left_armor - t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(1,panzer_end_left_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(1, panzer_left_armor)

        if hit_chance(author, receiver) is True:
            t34_end_right_armor = t34_left_armor- panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(2,t34_end_right_armor)
        else:
            print("MISS")
            t34_end_stats.insert(2, t34_left_armor)

        author = "T34"
        receiver = 'Panzer'
        if hit_chance(author, receiver) is True:
            panzer_end_right_armor = panzer_right_armor - t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(2,panzer_end_right_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(2, panzer_right_armor)

        if hit_chance(author, receiver) is True:
            t34_end_rear_armor = t34_rear_armor - panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(3,t34_end_rear_armor)
        else:
            print("MISS")
            t34_end_stats.insert(3, t34_rear_armor)
        author = "T34"
        receiver = 'Panzer'
        if hit_chance(author, receiver) is True:
            panzer_end_rear_armor = panzer_rear_armor - t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(3,panzer_end_rear_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(3, panzer_rear_armor)

    elif coin_flip() == "T34":
        author = "T34"
        receiver = 'Panzer'
        if hit_chance(author, receiver) is True:
            panzer_end_front_armor = panzer_front_armor - t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(0,panzer_end_front_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(0, panzer_front_armor)


        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            t34_end_front_armor = t34_front_armor - panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(0,t34_end_front_armor)
        else:
            print("MISS")
            t34_end_stats.insert(0, t34_front_armor )

        if hit_chance(author, receiver) is True:
            panzer_end_left_armor = panzer_left_armor - t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(1,panzer_end_left_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(1, panzer_left_armor)

        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            t34_end_left_armor = t34_left_armor- panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(1,t34_end_left_armor)
        else:
            print("Miss")
            t34_end_stats.insert(1, t34_left_armor)

        if hit_chance(author, receiver) is True:
            panzer_end_right_armor = panzer_right_armor- t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(2,panzer_end_right_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(2, panzer_right_armor)

        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            t34_end_right_armor = t34_right_armor- panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(2,t34_end_right_armor )
        else:
            print("MISS")
            t34_end_stats.insert(2, t34_right_armor)

        if hit_chance(author, receiver) is True:
            panzer_end_rear_armor = panzer_rear_armor- t34_damage[0]
            print("Panzer tank was hit")
            panzer_end_stats.insert(3,panzer_end_rear_armor)
        else:
            print("MISS")
            panzer_end_stats.insert(3, panzer_rear_armor)

        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            t34_end_rear_armor = t34_rear_armor - panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(3,t34_end_rear_armor)
        else:
            print("MISS")
            t34_end_stats.insert(3, t34_rear_armor)
    print(t34_end_stats)
    print(panzer_end_stats)


opening_round()