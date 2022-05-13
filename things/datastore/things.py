def get_all_things(db):
    rows = db.execute('SELECT * from things').fetchall()
    things = []
    if rows and len(rows) > 0:
        for row in rows:
            things.append(dict(row))
    return things
