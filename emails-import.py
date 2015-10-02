import csv
import sqlite3

file_in = "basf.csv"
file_log = "basf_log.txt"
db_file = "contacts-db.sqlite"

with open(file_log, 'wb') as logfile:
  with open(file_in, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    
    connection = sqlite3.connect(db_file)
    connection.text_factory = str
    cursor = connection.cursor()

    for row in reader:
      mail = row["Email"]
      parts = mail.split("@")
      parts = [a.split(".") for a in parts]
      firstname = parts[0][0]
      lastname = ""
      if len(parts[0]) > 1:
	lastname = parts[0][1]
      comp = parts[1][0]
      cursor.execute("SELECT COUNT(ID) FROM Contacts WHERE FirstName = ? AND LastName = ?",(firstname, lastname))
      if cursor.fetchone()[0] == 0:
	connection.execute("INSERT INTO Contacts (FirstName, LastName, Company, CommunicationState, EmailAddress, DateContacted) VALUES (?, ?, ?, 0, ?, date('now'))", (firstname, lastname, comp, mail))
	logfile.write("Added {} {}\n".format(firstname, lastname))
      else:
	logfile.write("Skipped existing {} {}\n".format(firstname, lastname))
	
    connection.commit()
    connection.close()