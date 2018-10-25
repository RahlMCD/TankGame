import mysql.connector



def populate_initial_stats():
    mysql_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="tank_stats_db"
    )
    # This will include the defensive capabilities of the panzer tank
    my_cursor = mysql_db.cursor()
    try:
        my_cursor.execute("DROP TABLE panzer_tank_defensive")
    except Exception as e:
        pass
    finally:
        my_cursor.execute("CREATE TABLE panzer_tank_defensive (name VARCHAR(200),life INTEGER(10))")
        panzer_insert_sql = "INSERT INTO panzer_tank_defensive (name,life) VALUES (%s, %s)"
        panzer_defensive_stats = [('Front Armor', 100), ('Left Side Armor', 200), ('Right Side Armor', 250),
                                  ('Back Side Armor', 400)]
        my_cursor.executemany(panzer_insert_sql,panzer_defensive_stats)
    mysql_db.commit()

    # This will include the offensive capabilities of the panzer tank
    my_cursor = mysql_db.cursor()
    try:
        my_cursor.execute("DROP TABLE panzer_tank_offensive")
    except Exception as e:
        pass
    finally:
        my_cursor.execute("CREATE TABLE panzer_tank_offensive (name VARCHAR(200),damage INTEGER(10))")
        my_cursor.execute( "INSERT INTO panzer_tank_offensive (name,damage) VALUES ('Cannon', 33)")
    mysql_db.commit()


    # This will include the defensive capabilities of the t34 tank
    my_cursor = mysql_db.cursor()
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
    mysql_db.commit()


    # This will include the offensive capabilities of the t34 tank
    my_cursor = mysql_db.cursor()
    try:
        my_cursor.execute("DROP TABLE t34_tank_offensive")
    except Exception as e:
        pass
    finally:
        my_cursor.execute("CREATE TABLE t34_tank_offensive (name VARCHAR(200),damage INTEGER(10))")
        my_cursor.execute("INSERT INTO t34_tank_offensive (name,damage) VALUES ('Cannon', 32)")
    mysql_db.commit()


