import mysql.connector

mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "R@hl8047",
    database="tanks_db"
)


# This will retrieve the defensive specs for the tanks
my_cursor = mysql_db.cursor()
my_cursor.execute("SELECT life FROM panzer_tank_defensive")
panzer_defensive_stats = [item[0] for item in my_cursor.fetchall()]


my_cursor.execute("SELECT life FROM t34_tank_defensive")
t34_defensive_stats = [item[0] for item in my_cursor.fetchall()]



# This will retrieve damage stats for tanks
my_cursor = mysql_db.cursor()
my_cursor.execute("SELECT damage FROM panzer_tank_offensive")
panzer_damage = list(map(int, [item[0] for item in my_cursor.fetchall()]))
my_cursor = mysql_db.cursor()
my_cursor.execute("SELECT damage FROM t34_tank_offensive")
t34_damage = list(map(int, [item[0] for item in my_cursor.fetchall()]))