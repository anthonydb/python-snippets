# Store all files in a local directory to a server
# using FTP

from ftplib import FTP
import os

# ftp settings
settings = {
    'ftp': {
        'url': 'ftp.some-server.com',
        'username': 'your-account-name',
        'password': 'your-password',
        'remote-directory': '/path/to/files'
    }
}

# local paths
paths = {
   'local-directory': 'my-files/'
}

# list of local files
files = os.listdir(paths['local-directory'])

# connect and store
for f in files:
    ftp = FTP(settings['ftp']['url'])
    ftp.login(settings['ftp']['username'], settings['ftp']['password'])
    ftp.cwd(settings['ftp']['remote-directory'])
    ftp.storbinary('STOR ' + f, open(paths['local-directory'] + f, 'rb'))
    ftp.close()
