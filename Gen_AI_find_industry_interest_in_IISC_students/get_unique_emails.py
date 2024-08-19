
import pandas as pd
import numpy as np

df = pd.read_excel('recruters.xlsx')

emails = df['Email']

email_set = set()

for i in emails:
    a = i.split(';')
    for j in a:
        j = j.strip()
        if '@' not in j:
            print(f'{j} --> Is NOT an Email')
            continue
        email_set.add(j)

email_set = list(email_set)
emails_df = pd.DataFrame(email_set)
emails_df.to_excel('emails.xlsx', header=False, index=False)

