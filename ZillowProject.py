import pandas as pd
import os
from twilio.rest import Client

from ZillowScrape import do_the_thing
from dotenv import load_dotenv
load_dotenv()

#My wrok----------------------------------
do_the_thing('94618','newest')


new_csv = pd.read_csv('properties-94618.csv')
main_csv = pd.read_csv('Biglist.csv')

main_csv['address']
new_prop = []

for idx, new_hotness in new_csv.iterrows():
  if new_hotness.address in list(main_csv['address']):
   # print("GOT IT!")
   pass
  else: 
    new_prop.append(new_hotness)




# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)

for row in new_prop:
    main_csv.loc[len(main_csv.index)] = row
    main_csv.to_csv("Biglist.csv")
    message = client.messages \
                .create(
                     body= row.url,
                     from_='+14158779518',
                     to='+14159884881'
                 )

    print(message.sid)
print("GOODBYE")

