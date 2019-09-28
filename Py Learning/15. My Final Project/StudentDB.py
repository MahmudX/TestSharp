import sqlite3
import os


db = sqlite3.connect('studentDB.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS studentDB(
                ID INTEGER PRIMARY KEY, Name TEXT, District TEXT, 'Blood Group' TEXT
                )""")
cursor.execute(
    ''' SELECT * FROM sqlite_master WHERE type='table' AND name='studentDB' ''')
cursor.execute("SELECT COUNT(*) FROM studentDB")
sCOUNT = cursor.fetchone()[0]


def inValInput():
    print('Invalid Input.')
    print('Type \'exit()\' exit the program')
    print('Press enter to try again.')


def Create():
    print("How many student\'s you want to add?")
    n = int(input())
    print('ID Scheme:')
    sID = int(input())
    print('Starting Position')
    sPo = int(input())
    counter = 1
    while counter <= n:
        print(f'ID: {sID}{sPo}')
        print('Name: ', end=' ')
        sNAME = input()
        print('Distict: ', end=' ')
        bgDis = input()
        sDIS = bgDis if bgDis else ' '
        print('Blood Group: ', end=' ')
        bgTemp = input()
        sBG = bgTemp if bgTemp else ' '
        cursor.execute(f"""
                INSERT INTO studentDB (ID, Name, District, 'Blood Group') VALUES ('{sID}{sPo}','{sNAME}','{sDIS}', '{sBG}')
            """)
        db.commit()
        counter += 1
        sPo += 1
    print('All the student(s) added to the database successfully.\n')


def Lookup():
    print(f'There are {sCOUNT} student(s) in the database.\n')
    if sCOUNT:
        print('All the students are -\n')
        for row in cursor.execute("SELECT * FROM studentDB"):
            print(f'ID: {row[0]}')
            print(f'Name: {row[1]}')
            print(f'District: {row[2]}')
            print(f'Blood Group: {row[3]}\n')


def SingleLookup():
    if sCOUNT:
        print('Enter student\'s ID:')
        idTemp = int(input())
        for row in cursor.execute(f"SELECT * FROM studentDB WHERE ID = '{idTemp}'"):
            print(f'\nID: {row[0]}')
            print(f'Name: {row[1]}')
            print(f'District: {row[2]}')
            print(f'Blood Group: {row[3]}\n')
    else:
        print('Please add at least one student to the database first.\n')


def Update():
    if sCOUNT:
        print('Enter student\'s ID:')
        idTemp = int(input())
        tempName = input('Name: ')
        tempDis = input('Districe: ')
        tempBG = input('Blood Group: ')
        if tempName:
            cursor.execute(
                f'UPDATE studentDB SET Name=\'{tempName}\' WHERE ID=\'{idTemp}\'')
        if tempDis:
            cursor.execute(
                f'UPDATE studentDB SET District=\'{tempDis}\' WHERE ID=\'{idTemp}\'')
        if tempBG:
            cursor.execute(
                f'UPDATE studentDB SET \'Blood Group\'=\'{tempBG}\' WHERE ID=\'{idTemp}\'')
        db.commit()
        print('Updated Successfully.\n')
    else:
        print('There is no student to edit.\n')


def Delete():
    print('Enter ID: ', end=' ')
    tempID = int(input())
    cursor.execute(f'DELETE FROM studentDB WHERE ID= {tempID}')
    db.commit()
    print('Student Removed from the database successfully.\n')

def PrintMenu():
    print('Menu')
    print('1. Lookup the full Database')
    print('2. Lookup a student\'s information')
    print('3. Update a student\' information')
    print('4. Add student(s) to the database')
    print('5. Delete students to the database')
    print('6. Exit\n')

def main():
    closeTheApp = ''
    while closeTheApp != 'exit()':
        PrintMenu()
        try:
            print('Enter a choice:', end=' ')
            menuItem = int(input())
            print()

            if menuItem == 1:  # Lookup the full Database
                Lookup()
            elif menuItem == 2:  # Lookup a student's information
                SingleLookup()
            elif menuItem == 3:  # Update a student\' information
                Update()
            elif menuItem == 4:  # Add students to the database
                Create()
            elif menuItem == 5:  # Delete students to the database
                Delete()
            elif menuItem == 6:  # Exit sequence
                closeTheApp = 'exit()'
            else:
                inValInput()
                closeTheApp = input()
        except:
            inValInput()
            closeTheApp = input()


if __name__ == "__main__":
    main()
