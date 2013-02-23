# Fetch Twitter profile details from Twitter API into a SQLite DB

import twitter
import sqlite3
import os
from datetime import datetime

# Set the Twitter API authentication
api = twitter.Api(consumer_key='your-key',
                  consumer_secret='your-secret-key',
                  access_token_key='your-access-token',
                  access_token_secret='your-token-secret')

# These are the accounts for which you will fetch data
handles_list = [
    'chrisschnaars',
    'anthonydb',
    'usatoday'
]


# Function to add row to accounts table
def insert_db(handle, followers, description):
    conn = sqlite3.connect('social_data2.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO twaccounts VALUES (?,?,?,?);
        ''', (datetime.now(), handle, followers, description))
    conn.commit()
    conn.close()

# Create the database if it doesn't exist
if not os.path.exists('social_data2.db'):
    conn = sqlite3.connect('social_data2.db')
    conn.close()
else:
    pass

# Create the table if it's not in the db
conn = sqlite3.connect('social_data2.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS twaccounts
    (FetchDate Date, Handle Text, Followers Integer, Description Text)
    ''')
conn.commit()
conn.close()

# Iterate over handles and hit the API with each
for handle in handles_list:
    print 'Fetching @' + handle
    try:
        user = api.GetUser(handle)
        followers = user.GetFollowersCount()
        description = user.GetDescription()
        insert_db(handle, followers, description)
    except:
        print '-- ' + handle + ' not found'
