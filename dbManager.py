from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import pathlib
path = pathlib.Path(__file__).parent.resolve()
strPath = str(path)
db = TinyDB(strPath+'/db.json')
'''
#basic working with the database for later reference
#insert objects into default db
db.insert({'name':'bob','surName':'suge'})
db.insert({'name':'dave','surName':'randy'})
#create and insert objects into db table boats
table = db.table('boats')
table.insert({'name':'bob','surName':'ron'})
#print complete default table
print(db.all())
print('specific ones')
#making a query object
person = Query()
#searching default db table
print(db.search(person.name == 'bob'))
#searching table
print(table.search(person.name == 'bob'))
#drop db
'''
db.drop_tables()
