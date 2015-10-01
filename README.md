# linkedin Mailer

A semiautomated system for messaging lots of people.

Uses Python, SQlite. CSV files for in/output

##Setup

Enter the credentials for your gmail in `credentials.py`. 
Run `setup_db.py`

##Workflow

* Crawl data from linkedin using some tool, we use (TODO). Export to CSV.
* Run import script, ours is `import_crawl_dump.py`
* Run mail script: `send_mails.py`
* Check results in your mail account, enter into `mail_results.csv`
* Apply results to DB with `integrate_results.csv`

Add more company domains by entering them into `domains.csv` and running `add_domains.py`.
Check for prospects by running `create_domain_report.py`.

##Internals
Contact states:

0: Unprocessed  
1: Valid Mail  
2: Invalid Mail  
3: Responded  
