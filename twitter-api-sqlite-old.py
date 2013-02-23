# DEPRECATED // Uses old Twitter API that is deprecated.

# Fetch Twitter profile details from Twitter API into a SQLite DB

import requests
import sqlite3
import os
from datetime import datetime

# These are the accounts for which you will fetch data
handles_list = [
    'anthonydb',
    'nytimes',
    'capitalweather',
    'washingtonpost',
    'usatoday'
]

# The base url for the Twitter API
base_url = 'https://api.twitter.com/1/users/show.json?screen_name='


# Function to add a row to the twaccounts table in your SQLite DB
def insert_db(handle, followers, description):
    conn = sqlite3.connect('social_data.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO twaccounts VALUES (?,?,?,?);
        ''', (datetime.now(), handle, followers, description))
    conn.commit()
    conn.close()

# Create the SQLite database if it doesn't exist
if not os.path.exists('social_data.db'):
    conn = sqlite3.connect('social_data.db')
    conn.close()
else:
    pass

# Create the DB table if it's not there already
conn = sqlite3.connect('social_data.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS twaccounts
    (FetchDate Date, Handle Text, Followers Integer, Description Text)
    ''')
conn.commit()
conn.close()

# Iterate over user handles and hit the API with each
for user in handles_list:
    url = base_url + user + '&include_entities=true'
    print 'Fetching @' + user
    response = requests.get(url)
    profile = response.json()
    handle = profile['screen_name']
    followers = profile['followers_count']
    description = profile['description']
    insert_db(handle, followers, description)
