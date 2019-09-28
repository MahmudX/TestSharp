import sqlite3

print('Connect:')
db = sqlite3.connect('db-api.db')
cur = db.cursor()
print('Create:')
cur.execute('DROP TABLE IF EXISTS test')
cur.execute("""
            CREATE TABLE test (
                id INTEGER PRIMARY KEY, string TEXT, number INTEGER
            )
            """)
print('Insert row')
cur.execute("""
            INSERT INTO test (string, number) VALUES ('one', 1)
            """)
cur.execute("""
            INSERT INTO test (string, number) VALUES ('two', 2)
            """)
cur.execute("""
            INSERT INTO test (string, number) VALUES ('three', 3)
            """)
print('Commit')
db.commit()
cur.execute("SELECT COUNT(*) FROM test")
count = cur.fetchone()[0]
print(f'There are {count} rows in the table.')
print('Read')
for row in cur.execute("SELECT * FROM test"):
    print(row)
print('Drop Table.')
cur.execute("DROP TABLE test")
print('Close the DB')
db.close()


