# One way to add switches to scripts
# Usage: python optionparser-test.py -f

# Thanks to:
# http://www.alexonlinux.com/pythons-optparse-for-human-beings

from optparse import OptionParser

parser = OptionParser()
parser.add_option('-f', dest='file', default=False, action='store_true')
parser.add_option('-d', dest='db', default=False, action='store_true')

(options, args) = parser.parse_args()

if options.file == True:
    print 'File'
else: pass

if options.db == True:
    print 'DB'
else: pass
