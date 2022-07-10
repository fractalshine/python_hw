import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()
sqlite_query = """SELECT `title`
            FROM netflix
            WHERE title = ''
"""
cur.execute(sqlite_query)
executed_query = cur.fetchall()
counter_movie = executed_query[0][0]
counter_season = executed_query[1][0]

result = f"Снято фильмов {counter_movie}, снято сериалов {counter_season}"

con.close()

if __name__ == '__main__':
    print(result)
