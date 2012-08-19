# Fetch Facebook page metrics via Social Graph API into a SQLite DB
# Grabs the number of likes and "talking about" numbers

import requests
import sqlite3
import os
from datetime import datetime

# These are the accounts for which you will fetch data
names_list = [
    'fallingskies',
    'usatoday'
]

# API base URL
base_url = 'https://graph.facebook.com/'

# Function to add row to accounts table
def insert_db(handle, likes, talking):
    conn = sqlite3.connect('social_data.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO fbaccounts VALUES (?,?,?,?);
        ''', (datetime.now(), handle, likes, talking))
    conn.commit()
    conn.close()

# Create the database if it doesn't exist
if not os.path.exists('social_data.db'):
    conn = sqlite3.connect('social_data.db')
    conn.close()
else:
    pass

# Create the table if it's not in the db
conn = sqlite3.connect('social_data.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS fbaccounts 
    (FetchDate Date, Handle Text, Likes Integer, Talking Integer)
    ''')
conn.commit()
conn.close()

# Iterate over handles and hit the API with each
for user in names_list:
    url = base_url + user 
    print 'Fetching ' + user
    response = requests.get(url)
    profile = response.json
    handle = profile['name']
    likes = profile['likes']
    talking = profile['talking_about_count']
    insert_db(handle, likes, talking)
