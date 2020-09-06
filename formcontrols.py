# Display any form controls on a web page

import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_handle_robots(False)

url = "http://www.wordpress.com"
br.open(url)
if br.forms():
    for form in br.forms():
        print "--------------------"
        print "Form name : " + str(form.name) 
        br.select_form(name=form.name)
    
        # loop through the controls in the form
        print "Controls:"
        for control in br.form.controls:
            if not control.name:
                print " - (type) =", (control.type)
                continue
            
            print " - (name, type, value) =", (control.name, control.type, br[control.name])

            # loop through all the options in any select (drop-down) controls
            if control.type == 'select':
                for item in control.items:
                    print " - - - (value, labels) =", (str(item), [label.text  for label in item.get_labels()])

