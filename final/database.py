import sqlite3

def insert_fetch():
    link = []
    conn = sqlite3.connect('db.sqlite')

    cur = conn.cursor()
    cur.execute('CREATE TABLE res (name text, description text)')

    cur.execute('INSERT INTO res (name, description) values ("Coreanos", "https://www.yelp.com/biz/coreanos-allston-allston?osq=coreanos")')
    conn.commit()

    cursor = conn.execute("SELECT name, description from res")
    for row in cursor:
        link.append(row[1])
        print("The restaurant is: "+row[0]+" .Its link is: " + row[1])
    conn.close()
    return

insert_fetch()

