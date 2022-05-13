from bottle import get
from things.datastore import things as store


@get('/things')
def get_things(db):
    return dict(things=store.get_all_things(db))

