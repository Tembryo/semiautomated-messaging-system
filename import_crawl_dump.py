import csv
import sqlite3

file_in = "persons_01-10-2015.csv"
file_log = "log_crawl_import.txt"
db_file = "contacts-db.sqlite"

with open(file_log, 'wb') as logfile:
  with open(file_in, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    
    connection = sqlite3.connect(db_file)
    connection.text_factory = str
    cursor = connection.cursor()

    for row in reader:
      if row["Company"] is "":
	logfile.write("Skipped no company\n")
	continue
      
      cursor.execute("SELECT COUNT(ID) FROM Contacts WHERE FirstName = ? AND LastName = ?",(row["First Name"], row["Last Name"]))
      if cursor.fetchone()[0] == 0:
	connection.execute("INSERT INTO Contacts (FirstName, LastName, Company, CommunicationState, EmailAddress, GroupInfo) VALUES (?, ?, ?, 0, '', date('now'))", (row["First Name"], row["Last Name"], row["Company"]))
	logfile.write("Added {} {}\n".format(row["First Name"], row["Last Name"]))
      else:
	logfile.write("Skipped existing {} {}\n".format(row["First Name"], row["Last Name"]))
	
    connection.commit()
    connection.close()