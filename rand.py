import random

x = 1

outfile = open('randomtest.txt','ab')

while x <= 40000:
    num = random.randint(1, 9)
    print x
    print >> outfile, str(num) + '\r\n'
    x += 1

outfile.close()
