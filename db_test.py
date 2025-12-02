import sqlite3

db_path = "/Users/jaypark/Desktop/Computer Science Project/Cosmetic Ingredients.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 1. See what tables are in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables in this database:", tables)

# If cosmetics is there, read first 5 rows
cur.execute("SELECT * FROM cosmetics LIMIT 5;")
rows = cur.fetchall()

print("\nFirst 5 rows in 'cosmetics':")
for r in rows:
    print(r)

conn.close()
