import sqlite3


def generate_placeholder(items):
    "Создает последовательность вопросиков"
    return ",".join(["?"] * len(items))


con = sqlite3.connect("source.db")

cur = con.cursor()

allowed_list = ("Banana", "Donut", "Cake")

query = "SELECT * FROM shop WHERE `name` in (" + generate_placeholder(allowed_list) + ")"

cur.execute(query, allowed_list)

result = cur.fetchall()

print(result)
con.close()
