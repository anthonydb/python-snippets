# Hit the Twitter API and pull either the public timeline or a user
# timeline, and then print a selection of data.
# UTF-8 encoding is necessary especially when dealing with public
# timeline.

# Use the requests module
import twitter

api = twitter.Api(consumer_key='RtrhKyhOal08VTHWVlEPKw',
                  consumer_secret='vb7fgiNSiF4x2zZIek2yGPxQfzJgQO6dRYoUeiuhBg',
                  access_token_key='18682941-4hd33e9dtYVWDScSyhc0dx9AVl7pQ4s7V2EbV8zjV',
                  access_token_secret='whz6Qc3MUWUtOMqBCr3UhiZ1LiyPahkTiYnD52OWBeQ')

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
