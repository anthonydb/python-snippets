# This is an update to the code Ben Welsh presented in his excellent
# web scraping tutorial at:
# http://palewi.re/posts/2008/04/20/python-recipe-grab-a-page-scrape-a-table-download-a-file/
# This version updates to Beautiful Soup 4 and uses requests

from mechanize import Browser
from bs4 import BeautifulSoup
import os
import requests

def extract(soup, year):
    table = soup.find("table", border=1)
    for row in table.find_all('tr'):
        col = row.find_all('td')

        rank = col[0].string
        artist = col[1].string
        album = col[2].string
        if col[3].string:
            cover_link = col[3].string
        else:
            cover_link = "http://www.palewire.com" + col[3].img['src']
        record = (str(year), rank, artist, album, cover_link)

        print >> outfile, "|".join(record)

        #save_as = os.path.join("./", album + ".jpg")
        if col[3].string:
            pass
        else:
            r = requests.get(cover_link)
            j = artist[0:4] + '-' + album[0] + '.jpg'
            with open(j, 'wb') as f:
                f.write(r.content)
        print "Downloaded %s album cover" % album
#        print "url is %s" % cover_link

outfile = open("albums.txt", "w")


mech = Browser()
url = "http://www.palewire.com/scrape/albums/2007.html"

page1 = mech.open(url)
html1 = page1.read()
soup1 = BeautifulSoup(html1)
extract(soup1, 2007)

page2 = mech.follow_link(text_regex="Next")
html2 = page2.read()
soup2 = BeautifulSoup(html2)
extract(soup2, 2006)

outfile.close()
