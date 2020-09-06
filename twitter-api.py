# Use the python-twitter library to authenticate with the Twitter API,
# fetch a user, and then print a selection of data. After that, fetch
# a user timeline and print some statuses.

import twitter

api = twitter.Api(consumer_key='J3F9fHP2O3uGktYgZBpPwQ',
                  consumer_secret='Fks5IfWRd44wPGPKowLXgJd71CN016FRBxg1v8QcU',
                  access_token_key='18682941-MYSJikMeMHkkYAkt84JvLxxJGQ5QCgfbdH8CKJJ4',
                  access_token_secret='DhDFftDP4MDxDbzZpm9aBJUQyKvi2JQ708mGXmtyU')

# set a handle
handle = 'anthonydb'

# Get some info on a user
user = api.GetUser(screen_name=handle)

print user.GetName()
print user.GetDescription()
print user.GetFollowersCount()
print user.GetStatusesCount()
print user.GetUrl()

# get a user timeline
statuses = api.GetUserTimeline(screen_name='pokjournal', count=2)
print [s.text for s in statuses]

