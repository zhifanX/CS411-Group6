import sqlite3

def insert_fetch():
    link = []
    conn = sqlite3.connect('db.sqlite')

    cur = conn.cursor()
    cur.execute('CREATE TABLE res (name text, description text)')

    cur.execute('INSERT INTO res (name, description) values ("ice", "http://")')
    conn.commit()

    cursor = conn.execute("SELECT name, description from res")
    for row in cursor:
        link.append(row[1])
    conn.close()
    return (row[1])

insert_fetch()

