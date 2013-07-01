# Hit the Twitter API and pull either the public timeline or a user
# timeline, and then print a selection of data.
# UTF-8 encoding is necessary especially when dealing with public
# timeline.

import twitter

api = twitter.Api(consumer_key='your-consumer-key',
                  consumer_secret='your-consumer-secret',
                  access_token_key='your-access-token-key',
                  access_token_secret='your-access-token-secret')

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
statuses = api.GetUserTimeline(screen_name='usatoday', count=1)
print [s.text for s in statuses]

