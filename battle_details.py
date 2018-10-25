import random

import mysql.connector

mysql_results = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "password",
    database="results_db"
)

mysql_stats = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "password",
    database="tank_stats_db"
)
# This will retrieve the defensive specs for the tanks
my_cursor = mysql_stats.cursor()
my_cursor.execute("SELECT life FROM panzer_tank_defensive")
panzer_defensive_stats = [item[0] for item in my_cursor.fetchall()]


my_cursor.execute("SELECT life FROM t34_tank_defensive")
t34_defensive_stats = [item[0] for item in my_cursor.fetchall()]



# This will retrieve damage stats for tanks
my_cursor = mysql_stats.cursor()
my_cursor.execute("SELECT damage FROM panzer_tank_offensive")
panzer_damage = list(map(int, [item[0] for item in my_cursor.fetchall()]))


my_cursor = mysql_stats.cursor()
my_cursor.execute("SELECT damage FROM t34_tank_offensive")
t34_damage = list(map(int, [item[0] for item in my_cursor.fetchall()]))
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
        first_to_shoot = 1
        # We ll name panzer as 1
    else:
        first_to_shoot = 2
        # we ll name t34 as 2
    return first_to_shoot


# This will choose which part of the armor it will hit
def target_choice(armor):
    x = random.randint(0,3)
    while armor[x] > 0 :
        target_armor = armor[x]
        return target_armor


# This will determine the chance each tank has to hit its target. This can be redefined to take into consideration
# more aspects, like speed
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
    if coin_flip() == 1:
        author = "Panzer"
        receiver = 'T34'
        if hit_chance(author, receiver) is True:
            t34_end_front_armor = t34_front_armor - panzer_damage[0]
            print("T34 tank was hit")
            t34_end_stats.insert(0, t34_end_front_armor)
        else:
            print("MISS")
            t34_end_stats.insert(0, t34_front_armor)

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

    elif coin_flip() == 2:
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
            t34_end_stats.insert(0, t34_front_armor)

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

    panzer = panzer_end_stats
    print(panzer)
    t34 = t34_end_stats
    print(t34)
    return panzer, t34


