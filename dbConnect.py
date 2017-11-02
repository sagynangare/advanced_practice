import sqlite3

def Main():
    con =sqlite3.connect('sagTest.db')
    c = con.cursor()
    c.execute('SELECT SQLITE_VERSION()')
    data = c.fetchone()

    print(data)

    con.close()

if __name__=='__main__':
    Main()
