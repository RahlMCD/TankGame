import mysql.connector


battle_results = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "password",
    database= "battle_results"
)

# Once you have the final results of the battle you need to store them in the results db
# First we store the Panzer stats
my_cursor = battle_results.cursor()
try:
    my_cursor.execute("DROP TABLE battle_results_panzer")
except Exception as e:
    pass
finally:
    my_cursor.execute("CREATE TABLE battle_results_panzer (name VARCHAR(200),life INTEGER(10))")
battle_results.commit()

# Last we store the T34 stats
my_cursor = battle_results.cursor()
try:
    my_cursor.execute("DROP TABLE battle_results_t34")
except Exception as e:
    pass
finally:
    my_cursor.execute("CREATE TABLE battle_results_t34 (name VARCHAR(200),life INTEGER(10))")
battle_results.commit()

