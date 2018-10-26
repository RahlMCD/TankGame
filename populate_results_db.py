import mysql.connector

def populate_results():
    results_db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password="password",
        database = "results_db"
    )
    my_cursor = results_db.cursor()
    my_cursor.execute("CREATE TABLE battle_results_panzer (name VARCHAR(200),life INTEGER(10))")
    panzer_insert_sql = "INSERT INTO battle_results_panzer (name,life) VALUES (%s, %s)"
    panzer_defensive_stats = [('Front Armor', 100), ('Left Side Armor', 200), ('Right Side Armor', 250),
                              ('Back Side Armor', 400)]
    my_cursor.executemany(panzer_insert_sql, panzer_defensive_stats)
    results_db.commit()

    my_cursor = results_db.cursor()
    my_cursor.execute("CREATE TABLE battle_results_t34 (name VARCHAR(200),life INTEGER(10))")
    t34_insert_sql = "INSERT INTO battle_results_t34 (name,life) VALUES (%s, %s)"
    t34_defensive_stats = [('Front Armor', 100), ('Left Side Armor', 200), ('Right Side Armor', 300),
                           ('Back Side Armor', 400)]
    my_cursor.executemany(t34_insert_sql, t34_defensive_stats)
    results_db.commit()
