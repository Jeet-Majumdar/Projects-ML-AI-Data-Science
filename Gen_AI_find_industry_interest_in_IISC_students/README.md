# Find Industry Interest in IISC students

Here I was using all the mails that were send from IISC to different recruiters 

Approach:

1. Scrape all the mails using `scrape_outlook_inbox.py` 
2. Construct a csv/xlsx file with name of company, recruiter's email id, and other detail as per use
3. Use HuggingFace model to use the company name and find the industry the company belongs to
4. Append the industry column with company name
5. Analyse

