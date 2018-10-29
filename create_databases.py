import mysql
from mysql import connector


# Create initial tank stats db and results db
def create_database_init():
    init_db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password="R@hl8047"
    )
    my_cursor = init_db.cursor()
    try:
        my_cursor.execute("CREATE DATABASE tank_stats_db")
    except Exception as e:
        pass
    init_db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password="R@hl8047",
        database= "tank_stats_db"
    )
    my_cursor = init_db.cursor()
    try:
        my_cursor.execute("DROP TABLE panzer_tank_defensive")
    except Exception as e:
        pass
    my_cursor.execute("CREATE TABLE panzer_tank_defensive (name VARCHAR(200),life INTEGER(10))")
    panzer_insert_sql = "INSERT INTO panzer_tank_defensive (name,life) VALUES (%s, %s)"
    panzer_defensive_stats = [('Front Armor', 100), ('Left Side Armor', 200), ('Right Side Armor', 250),
                              ('Back Side Armor', 400)]
    my_cursor.executemany(panzer_insert_sql, panzer_defensive_stats)
    init_db.commit()
    my_cursor = init_db.cursor()
    try:
        my_cursor.execute("DROP TABLE panzer_tank_offensive")
    except Exception as e:
        pass
    finally:
        my_cursor.execute("CREATE TABLE panzer_tank_offensive (name VARCHAR(200),damage INTEGER(10))")
        my_cursor.execute( "INSERT INTO panzer_tank_offensive (name,damage) VALUES ('Cannon', 33)")
    init_db.commit()

    # This will include the defensive capabilities of the t34 tank
    my_cursor = init_db.cursor()
    try:
        my_cursor.execute("DROP TABLE t34_tank_defensive")
    except Exception as e:
        pass
    finally:
        my_cursor.execute("CREATE TABLE t34_tank_defensive (name VARCHAR(200),life INTEGER(10))")
        t34_insert_sql = "INSERT INTO t34_tank_defensive (name,life) VALUES (%s, %s)"
        t34_defensive_stats = [('Front Armor', 100), ('Left Side Armor', 200), ('Right Side Armor', 300),
                               ('Back Side Armor', 400)]
        my_cursor.executemany(t34_insert_sql, t34_defensive_stats)
    init_db.commit()

    # This will include the offensive capabilities of the t34 tank
    my_cursor = init_db.cursor()
    try:
        my_cursor.execute("DROP TABLE t34_tank_offensive")
    except Exception as e:
        pass
    finally:
        my_cursor.execute("CREATE TABLE t34_tank_offensive (name VARCHAR(200),damage INTEGER(10))")
        my_cursor.execute("INSERT INTO t34_tank_offensive (name,damage) VALUES ('Cannon', 32)")
    init_db.commit()


def create_database_results():
    results_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password="R@hl8047"
    )
    my_cursor = results_db.cursor()
    try:
        my_cursor.execute("CREATE DATABASE results_db")
    except Exception as e:
        pass

    results_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password="R@hl8047",
        database = "results_db"
    )
    my_cursor = results_db.cursor()
    try:
        my_cursor.execute("DROP TABLE battle_results_panzer ")
    except Exception as e:
        pass
    my_cursor.execute("CREATE TABLE battle_results_panzer (name VARCHAR(200),life INTEGER(10))")
    panzer_insert_sql = "INSERT INTO battle_results_panzer (name,life) VALUES (%s, %s)"
    panzer_defensive_stats = [('Front Armor', 100), ('Left Side Armor', 200), ('Right Side Armor', 250),
                              ('Back Side Armor', 400)]
    my_cursor.executemany(panzer_insert_sql, panzer_defensive_stats)
    results_db.commit()

    my_cursor = results_db.cursor()
    try:
        my_cursor.execute("DROP TABLE battle_results_t34")
    except Exception as e:
        pass
    my_cursor.execute("CREATE TABLE battle_results_t34 (name VARCHAR(200),life INTEGER(10))")
    t34_insert_sql = "INSERT INTO battle_results_t34 (name,life) VALUES (%s, %s)"
    t34_defensive_stats = [('Front Armor', 100), ('Left Side Armor', 200), ('Right Side Armor', 300),
                           ('Back Side Armor', 400)]
    my_cursor.executemany(t34_insert_sql, t34_defensive_stats)
    results_db.commit()


create_database_init()