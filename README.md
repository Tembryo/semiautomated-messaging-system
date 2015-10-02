# Semiautomated Person Acquisition Module

A semiautomated system for messaging lots of people, using name/company data scraped from the web.  
The Semiautomated Person Acquisition Module (SPAM) system helps you to automatically send emails and keep track of the results.

Uses Python, SQlite, CSV files for batch in/output.

We highly recommend setting up an GUI program to be able to manually fix/update stuff in the database.

##Setup

Enter the credentials for your gmail in `credentials.py`.  
Run `setup_db.py`  
Make sure you set up your Gmail account to allow the script to login. 
[This](http://stackoverflow.com/questions/10147455/trying-to-send-email-gmail-as-mail-provider-using-python/27515833#27515833) might help,
also double check that you change the settings for the correct gmail account.

##Workflow

* Crawl data from linkedin using some tool, we use [Salestools](https://salestools.io/). Be aware though that they seem to have issues with various OSes (we had to bring out an old Windows7 laptop).  
  Export to CSV.
* Run import script, ours is `import_crawl_dump.py`
* Run mail script: `send_mails.py`
* Check results in your mail account, enter into `mail_results.csv`
* Apply results to DB with `integrate_results.csv`

Add more company domains by entering them into `domains.csv` and running `add_domains.py`.
Check for prospects by running `create_domain_report.py`.

Add lists of emails by running `emails-import.py`.

##Internals

Emails are generated as FirstName.LastName@company.com  
Optionall, if a domain for the company has been specified, FirstName.LastName@domain is used.  
All special characters are removed, last names/company names are reduced to only their first part (separated by whitespace).  

Contact states:

0: Unprocessed  
1: Valid Mail  
2: Invalid Mail  
3: Responded  
4: LinkedIn contact (no email, but dont contact)  
5: Closed good__

## License

This repository is made available under the

    /*
    * ---------------------------------------------------------------------------------------------
    * "A PIZZA-WARE LICENSE" (Revision ??):
    * As long as you retain this notice you can do whatever you want with this stuff.
    * If we meet some day, and you think this stuff is worth it,
    * you can buy me a pizza in return.
    *    Quirin Fischer
    * ---------------------------------------------------------------------------------------------
    */