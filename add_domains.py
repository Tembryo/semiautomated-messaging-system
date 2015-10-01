import csv
import sqlite3

file_in = "domains.csv"
file_log = "domain_import_log.txt"
db_file = "contacts-db.sqlite"

with open(file_log, 'wb') as logfile:
  with open(file_in, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    
    connection = sqlite3.connect(db_file)
    connection.text_factory = str
    cursor = connection.cursor()

    for row in reader:
      connection.execute("INSERT INTO Domains (Company, MailDomain) VALUES (?, ?)", (row["Company"], row["Domain"]))
      logfile.write("Added {} {}\n".format(row["Company"], row["Domain"]))
	
    connection.commit()
    connection.close()