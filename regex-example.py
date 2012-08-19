# regex examples
# For reference: http://www.regular-expressions.info/reference.html/
# To test regexes: http://regexpal.com/

import re

# text to parse
text1 = 'Monday, June 4, 1997, 2:38 p.m.'
text2 = 'Thursday, March 31, 2011, 12:38 a.m.'

# match the time
time1 = re.search('\d{1,2}:\d{2} (a.m.|p.m.)', text1)
time2 = re.search('\d{1,2}:\d{2} (a.m.|p.m.)', text2)

print 'The time is ' + time1.group()
print 'The time is ' + time2.group()

# match the day
day1 = re.search('[^,]*', text1)
day2 = re.search('[^,]*', text2)

print 'The day is ' + day1.group()
print 'The day is ' + day2.group()

# match the date
date1 = re.search('\w+ \d{1,2}, \d{4}', text1)
date2 = re.search('\w+ \d{1,2}, \d{4}', text2)

print 'The date is ' + date1.group()
print 'The date is ' + date2.group()

# match it all
match1 = re.search('([^,]*), (\w+ \d{1,2}, \d{4}), (\d{1,2}:\d{2}) (a.m.|p.m.)', text1)
match2 = re.search('([^,]*), (\w+ \d{1,2}, \d{4}), (\d{1,2}:\d{2}) (a.m.|p.m.)', text2)

print 'Day: ' + match1.group(1) + '; Date: ' + match1.group(2) +  \
      '; Time: ' + match1.group(3) + ' ' + match1.group(4)
print 'Day: ' + match2.group(1) + '; Date: ' + match2.group(2) +  \
      '; Time: ' + match2.group(3) + ' ' + match2.group(4)

# Another example
form1 = 'Name: Bob Michaels'
form2 = 'Name: Pam Wells'
form3 = 'Name: Bono'

namematch1 = re.search('Name: (.*)', form1)
namematch2 = re.search('Name: (.*)', form2)
namematch3 = re.search('Name: (.*)', form3)

print namematch1.group(1)
print namematch2.group(1)
print namematch3.group(1)
