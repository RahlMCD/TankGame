import mysql.connector


# Create initial tank stats db and results db
def create_databases():
    results_db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password="password"
    )
    my_cursor = results_db.cursor()
    try:
        my_cursor.execute("CREATE DATABASE results_db")
    except Exception as e:
        pass
    try:
        my_cursor.execute("CREATE DATABASE tank_stats_db")
    except Exception as e:
        pass
    results_db.commit()



