import re
import win32com.client as client
import pandas as pd

outlook = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#Accessing mail box
root_folder = outlook.Folders.Item('jeetmajumdar@iisc.ac.in')

#inbox messges
print("reading Inbox...")
Inbox = root_folder.Folders['Placement']
messages = Inbox.items

company_emails = ""
with open('recruters.csv', 'w') as f:
    f.write(f"Date,Name,Company,Email\n")
    for m in messages:
        item_subject = m.Subject
        if "IISc || Full time Placement Invite 2024-25" in item_subject:
            company = item_subject.split('||')[-1].replace('\n', '').replace(',', '')
            company = re.sub('[^0-9a-zA-Z]+', '', company)
            to = str(m.To).replace('\n', '').replace(',', '')
            sender = str(m.SenderEmailType).replace('\n', '').replace(',', '')
            date = m.SentOn.strftime('%d-%m-%Y')
            body = str(m.Body)
            try:
                name = body.split('\n')[0].replace(',', '').replace('To:', '')\
                    .replace(':', '').replace('Hello', '').replace('Dear', '').strip()
                name = re.sub('[^0-9a-zA-Z]+', '', name)
                statement = f"{date},{name},{company},{to}"
                company_emails += f"{to} "
                f.write(f"{statement}\n")
                print(statement)
            except:
                try:
                    name = ""
                    statement = f"{date},{name},{company},{to}"
                    company_emails += f"{to} "
                    f.write(f"{statement}\n")
                    print(statement)
                except:
                    name = ""
                    statement = f",,{company},{to}"
                    company_emails += f"{to} "
                    f.write(f"{statement}\n")
                    print(statement)

            
            

# print(company_emails)