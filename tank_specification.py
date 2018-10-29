import mysql.connector


mysql_stats = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="R@hl8047",
    database="tank_stats_db"
)

my_cursor = mysql_stats.cursor()
my_cursor.execute("SELECT * FROM panzer_tank_defensive")
results = my_cursor.fetchall()
my_cursor.execute("SELECT * FROM t34_tank_defensive")
results2 = my_cursor.fetchall()

