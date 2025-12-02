import sqlite3

db_path = "/Users/jaypark/Desktop/Cosmetic Ingredients.db"  # if the real one is there
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables in this database:", tables)

conn.close()
