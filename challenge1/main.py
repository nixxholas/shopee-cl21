import pandas as pd

df = pd.read_json('contacts.json')
df.head()

for datumFrame in df:
    print(datumFrame)