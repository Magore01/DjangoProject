import _mysql_connector

from DjangoProject.settings import DATABASES

db= _mysql_connector.connect(
    host= 'localhost',
    user= 'username',
    password= 'password',
)
print(db)
cursor = db.cursor()
cursor. excute ("Create DATABASES")
cursor.excute("showdatabases")
for x in cursor:
    print(x)
    