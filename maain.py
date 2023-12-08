# Use this web service
# https://jsonplaceholder.typicode.com/users
# and make a program that get all users data including
# name, username, email, street, suite, city, zip code, geo_lat & geo_long
# and then save them in a CSV file.
import requests
import csv
import pandas as pd

data = requests.get('https://jsonplaceholder.typicode.com/users')
data = data.json()
print(data)
with open('make.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'username', 'email', 'street', 'suite', 'city', 'zip code', 'geo_lat', 'geo_long'])
    for user in data:
        address = user.get('address', {})
        geo = address.get('geo', {})

        writer.writerow([user.get('id', ''),
                         user.get('name', ''),
                         user.get('username', ''),
                         user.get('email', ''),
                         address.get('street', ''),
                         address.get('suite', ''),
                         address.get('city', ''),
                         address.get('zipcode', ''),
                         geo.get('lat', ''),
                         geo.get('lng', '')])
a = pd.read_csv('make.csv')
print(a)
