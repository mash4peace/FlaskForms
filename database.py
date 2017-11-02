import sqlite3
def createdb():
    conn = sqlite3.connect("database.db")
    print("Opened database successfully!!")
    conn.execute('Create Table If not EXISTS users (id INTEGER  PRIMARY Key Autoincrement , name Text NOT NULL ,email text NOT NULL ,password Text NOT NULL )')

    conn.execute("INSERT INTO users VALUES (1, 'Mohamed', 'mash@gmail', 'pabs')")

    print("Table were created succesfully")
    for r in conn.execute('SELECT * from users'):
        print(r)

    conn.close()
