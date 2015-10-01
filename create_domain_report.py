import sqlite3
import csv


file_result = "domain_report.txt"

db_file = "contacts-db.sqlite"
connection = sqlite3.connect(db_file)
connection.text_factory = str

cursor = connection.cursor()

cursor.execute("SELECT Company, COUNT(*) FROM Contacts WHERE CommunicationState = 0 OR CommunicationState = 2 AND NOT  GROUP BY Company ORDER BY COUNT(*) DESC")
rows = cursor.fetchall()
with open(file_result, "wb") as reportfile:
  for row in rows:
      
      reportfile.write("{}: {}\n".format(row[0],row[1]))
      