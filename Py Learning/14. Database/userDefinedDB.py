import sqlite3

db = sqlite3.connect('IO.db')
cursor = db.cursor()
# cursor.execute("DROP TABLE IF EXISTS studentDB")
cursor.execute("""
                CREATE TABLE IF NOT EXISTS studentDB(
                    ID INTEGER PRIMARY KEY, Name TEXT, District TEXT
                )
                """)
cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='studentDB' ''')
# if cursor.fetchone()[0]==1 :
# 	print('Table exists.')
# else:
#     print('not found')


print("How many student's you want to add?")
n = int(input())
print('ID Scheme:')
sID = int(input())
print('Starting Position')
sPo = int(input())
counter = 1
while counter <= n:
    print('Name')
    sNAME = input()
    print('Distict')
    sDIS = input()
    cursor.execute(f"""
            INSERT INTO studentDB (ID, Name, District) VALUES ('{sID}{sPo}','{sNAME}','{sDIS}')
            """)
    db.commit()
    counter += 1
    sPo += 1

print("All the student's have been added to the database.")

cursor.execute("SELECT COUNT(*) FROM studentDB")
sCOUNT = cursor.fetchone()[0]
print(f'There are {sCOUNT} students in the database.')

print('All the students are -')
for row in cursor.execute("SELECT * FROM studentDB"):
    print(f'ID: {row[0]}')
    print(f'Name: {row[1]}')
    print(f'District: {row[2]}')

# print('Drop Table.')
# cursor.execute("DROP TABLE studentDB")
# print('Close the DB')
db.close()
