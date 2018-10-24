import mysql.connector

mysql_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "password",
    database="tanks_db"
)


# This will retrieve the defensive specs for the tanks
my_cursor = mysql_db.cursor()
my_cursor.execute("SELECT life FROM panzer_tank_defensive")
panzer_defensive_stats = [item[0] for item in my_cursor.fetchall()]
panzer_front_armor = panzer_defensive_stats[0]
panzer_left_armor = panzer_defensive_stats[1]
panzer_right_armot = panzer_defensive_stats[2]
panzer_rear_armor = panzer_defensive_stats[3]


my_cursor.execute("SELECT life FROM t34_tank_defensive")
t34_defensive_stats = [item[0] for item in my_cursor.fetchall()]
t34_front_armor = t34_defensive_stats[0]
t34_left_armor = t34_defensive_stats[1]
t34_right_armor = t34_defensive_stats[2]
t34_rear_armor = t34_defensive_stats[3]


# This will retrieve damage stats for tanks
my_cursor = mysql_db.cursor()
my_cursor.execute("SELECT damage FROM panzer_tank_offensive")
panzer_damage = list(map(int, [item[0] for item in my_cursor.fetchall()]))
my_cursor = mysql_db.cursor()
my_cursor.execute("SELECT damage FROM t34_tank_offensive")
t34_damage = list(map(int, [item[0] for item in my_cursor.fetchall()]))