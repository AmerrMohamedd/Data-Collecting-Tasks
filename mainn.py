# get the details of all the users from
# this api https://gorest.co.in/public-api/users
# from all the pages and save it to a csv file.
# (name,email,gender,status(0,1))
# then get the number of the active females in page 1.
import requests
import csv
import pandas as pd

info = requests.get('https://gorest.co.in/public-api/users')
info = info.json()

for page_n in range(1, 290):
    df = requests.get(f'https://gorest.co.in/public-api/users?page={page_n}').json()
    print(df)
active_females = []
with open('save.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'email', 'gender', 'status'])
    for user in info['data']:
        writer.writerow([user['name'], user['email'], user['gender'], user['status']])

ab = pd.read_csv('save.csv')
print(ab)

active_females = len(ab[(ab["status"] == "active") & (ab["gender"] == "female")])
print(f'Number of active females: {active_females}')
