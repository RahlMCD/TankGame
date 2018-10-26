import mysql.connector

from battle_details import *

results = opening_round()
panzer = results[0]
t34 = results[1]


def write_results():
    battle_results = mysql.connector.connect(
        host='localhost',
        user="root",
        password="password",
        database="results_db"
    )
    # Once you have the final results of the battle you need to store them in the results db
    # First we store the Panzer stats
    my_cursor = battle_results.cursor()
    panzer_insert_sql = "UPDATE battle_results_panzer SET life = %s WHERE name = %s"
    panzer_defensive = [(panzer[0],'Front Armor'), (panzer[1],'Left Side Armor'), (panzer[2],'Right Side Armor' ),
                        (panzer[3],'Back Side Armor')]
    my_cursor.executemany(panzer_insert_sql, panzer_defensive)
    battle_results.commit()

    # Last we store the T34 stats
    my_cursor = battle_results.cursor()
    t34_insert_sql = "UPDATE battle_results_t34 SET life = %s WHERE name = %s "
    t34_defensive_stats = [(t34[0],'Front Armor'), (t34[1],'Left Side Armor'), (t34[2],'Right Side Armor' ),
                           (t34[3],'Back Side Armor' )]
    my_cursor.executemany(t34_insert_sql, t34_defensive_stats)
    battle_results.commit()

