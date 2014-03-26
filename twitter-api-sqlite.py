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
# It's a list of lists, with a category added for each handle
handles_list = [
    ['chrisschnaars', 'journalist'],
    ['anthonydb', 'journalist'],
    ['usatoday', 'newsroom']
]

# Function to add row to accounts table
def insert_db(handle, category, followers, description):
    conn = sqlite3.connect('social_data2.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO twaccounts VALUES (?,?,?,?,?);
        ''', (datetime.now(), handle, category, followers, description))
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
    (FetchDate Date, Handle Text, Category Text, Followers Integer, Description Text)
    ''')
conn.commit()
conn.close()

#Iterate over handles and hit the API with each
for handle in handles_list:
    print 'Fetching @' + handle[0]
    try:
        user = api.GetUser(screen_name=handle[0])
        followers = user.GetFollowersCount()
        description = user.GetDescription()
        insert_db(handle[0], handle[1], followers, description)
    except:
        print '-- ' + handle[0] + ' not found'
