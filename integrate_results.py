import csv
import sqlite3

log_file = "log_integrate.txt"
integration_file = "mails_sent.csv"
db_file = "contacts-db.sqlite"
connection = sqlite3.connect(db_file)

with open(log_file, "wb") as logfile:
  with open(integration_file, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    count_good = 0
    count_bad = 0
    for row in reader:
      cursor = connection.cursor()
      
      if int(row["Valid"]) == 1 :#good email
	cursor.execute("UPDATE Contacts SET EmailAddress = ?, CommunicationState = ? WHERE ID = ?", (row["Address"], row["Valid"], row["ID"]))
	logfile.write("Added good address {} {} {} -> {}\n".format(row["FirstName"], row["LastName"], row["Address"], row["Valid"]))
	count_good += 1
      if int(row["Valid"]) == 2 :#bad email
	cursor.execute("UPDATE Contacts SET CommunicationState = ? WHERE ID = ?", (row["Valid"], row["ID"]))
	logfile.write("Noted bad address {} {} {} -> {}\n".format(row["FirstName"], row["LastName"], row["Address"], row["Valid"]))
	count_bad += 1
    connection.commit()
    connection.close()
    logfile.write("Imported {} good, {} bad".format(count_good, count_bad))