import sqlite3

conn = sqlite3.connect("mutual_fund_analytics.db")
cursor = conn.cursor()

with open("sql/05_views.sql", "r") as file:
    cursor.executescript(file.read())

conn.commit()

print("✅ Views created successfully!")

cursor.execute("SELECT name FROM sqlite_master WHERE type='view';")

print("\nViews in Database:\n")

for view in cursor.fetchall():
    print(view[0])

conn.close()