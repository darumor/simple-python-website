import hashlib


def create_user(db, firstname, lastname):
    cursor = db.execute(
        'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
        (firstname, lastname))
    row_count = cursor.rowcount
    if row_count > 0:
        user_id = cursor.lastrowid
    else:
        user_id = -1
    return dict(user_id=user_id)


def get_user_by_id(db, user_id):
    row = db.execute('SELECT * from users where id=?', (user_id,)).fetchone()
    if row:
        user = dict(row)
        return user
    return None

