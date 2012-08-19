# Hit the Twitter API and pull either the public timeline or a user 
# timeline, and then print a selection of data.
# UTF encording is necessary especially when dealing with public
# timeline.

# Use the requests module
import requests

# Ppen url for API
#j = requests.get('https://twitter.com/statuses/public_timeline.json')
j = requests.get('http://api.twitter.com/1/statuses/user_timeline.json?screen_name=anthonydb')

# Use requests' json method and iterate through range
tweets = j.json
for x in range(0,5):
    print x
    print 'Name: ' + tweets[x]['user']['name'].encode('UTF-8')
    print 'Lang: ' + tweets[x]['user']['lang'].encode('UTF-8')
    print 'Handle: ' + tweets[x]['user']['screen_name'].encode('UTF-8')
    print 'Description: ' + tweets[x]['user']['description'].encode('UTF-8')
    print 'Tweeted: ' + tweets[x]['text'].encode('UTF-8') + '\n'
    #print ''

# uncomment this section to print to file
#tweets = j.json
#jf = open('jsonoutfile.txt', 'wb')
#print >> jf, tweets[0]
#jf.close()

