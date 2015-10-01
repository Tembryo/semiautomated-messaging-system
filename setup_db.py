from sqlite_wrap import *

db_file = "contacts-db.sqlite"

connection = sqlite3.connect(db_file)

connection.execute("CREATE TABLE IF NOT EXISTS Contacts ("
		   "ID INTEGER PRIMARY KEY,"
		   "FirstName TEXT,"
		   "LastName TEXT,"
		   "Company TEXT,"
		   "CommunicationState TEXT,"
		   "EmailAddress TEXT,"
		   "DateContacted TEXT,"
		   "Notes TEXT)")

connection.execute("CREATE TABLE IF NOT EXISTS Domains ("
		   "Company TEXT,"
		   "MailDomain TEXT)"
		  )

connection.commit()

close(connection)