from cs50 import SQL
import csv
db = SQL("sqlite:///coding.db")

name = input("Name: ").strip()

rows = db.execute("SELECT COUNT(*) AS counter FROM coding WHERE Name LIKE ?", name)

row = rows[0]
print(row["counter"])

