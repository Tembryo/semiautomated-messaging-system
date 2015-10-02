import yagmail
import sqlite3
from credentials import get_login
import csv


file_log = "log_mails.txt"

db_file = "contacts-db.sqlite"
connection = sqlite3.connect(db_file)
connection.text_factory = str

def first_dot_last_at_domain(fn, ln, domain):
  return ["{}.{}@{}".format(fn, ln, domain)]

address_schemes = [first_dot_last_at_domain, ]

def create_address_candidates(fn, ln, domain):
  addresses = []
  for scheme in address_schemes:
    addresses.extend(scheme(fn, ln, domain))
  return addresses

subject = "Data Analysis Startup"

def create_message(fn, ln, domain):
  return "Dear {},\n\n"\
	 "I am the co-founder of a startup based in London that is developing software for fault detection in industrial production systems.\n"\
	 "We would love to get some feedback on what we are doing and discuss potential applications in your industry. Would you be available for a quick chat, or if not, perhaps you could refer us to someone else you think we should talk to?\n\n"\
	 "best wishes,\n"\
	 "Quirin Fischer, CTO at Tembryo".format(fn)



with open(file_log, "wb") as logfile:
  #fetch domains
  domain_dict = {}
  cursor = connection.cursor()
  
  cursor.execute("SELECT Company, MailDomain FROM Domains")
  domain_rows = cursor.fetchall()
  for row in domain_rows:
      domain_dict[row[0]] = row[1]
      
  gmail_name, gmail_pw = get_login()
  gmail_connection = yagmail.SMTP(gmail_name, gmail_pw)
  #do all people
  with open('mails_sent.csv', 'wb') as result_file:
    result_fields= ["ID", "FirstName", "LastName", "Address", "Valid"]
    writer = csv.DictWriter(result_file, fieldnames=result_fields)
    writer.writeheader()
    cursor.execute("SELECT ID, FirstName, LastName, Company, EmailAddress FROM Contacts WHERE CommunicationState = 0")
    rows = cursor.fetchall()
    for row in rows:
      
      fn = ''.join(e for e in row[1] if e.isalnum())
      if row[2] == "":
	ln = ""
      else:
	ln = row[2].split()[0]
      ln = ''.join(e for e in ln if e.isalnum())
      domain = ""
      company = row[3]
      if domain_dict.has_key(company):
	domain  = domain_dict[company]
      else:
	c = company.split()[0]
	c = ''.join(e for e in c if e.isalnum())
	domain = "{}.com".format(c)
	      
      for address in create_address_candidates(fn,ln,domain):
	if row[4] != "":
	  address = row[4]
	gmail_connection.send(address, subject, create_message(fn,ln, domain))
	result_row={"ID":row[0], "FirstName":row[1],"LastName":row[2],"Address":address,"Valid":0}
	writer.writerow(result_row)
	logfile.write("sent {}\n".format(address))
	print "sent {}\n".format(address)