import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("mutual_fund_analytics.db")

cursor = conn.cursor()

# Read SQL file
with open("sql/04_analysis_queries.sql", "r") as file:
    sql_script = file.read()

# Split into individual queries
queries = sql_script.split(";")

print("=" * 60)

for i, query in enumerate(queries):

    query = query.strip()

    if query:

        try:
            print(f"\nQuery {i+1}")

            cursor.execute(query)

            rows = cursor.fetchall()

            for row in rows[:10]:
                print(row)

            print("-" * 50)

        except Exception as e:
            print(e)

conn.close()