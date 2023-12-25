import duckdb
import csv

conn = duckdb.connect('data/footballs.db')
conn.execute("CREATE OR REPLACE TABLE rush AS SELECT * FROM 'data/results.csv'")
conn.table('rush').show()
query1 = "SELECT Player, Att FROM rush"

roster = conn.execute("SELECT Player FROM rush LIMIT 5").fetchall()
attempts = conn.execute(query1).fetchall()
print(attempts[2][0], attempts[2][1])