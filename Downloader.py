
'''
DOWNLOADER
Jeff Thompson | 2019 | jeffreythompson.org

A little utility that downloads the entire Diehard CD-ROM contents
from Wayback Machine's FTP archive. A little sloppy but gets the
job done :)

'''

import wget, os

download_folder = 'CD-ROM'
base_url = 'https://web.archive.org/web/20120729052013if_/http://www.stat.fsu.edu/pub/diehard/cdrom/'

if not os.path.exists(download_folder):
	os.mkdir(download_folder)

def download(folder, files):
	if folder != '' and not os.path.exists(folder):
		os.mkdir(os.path.join(download_folder, folder))
	for filename in files:
		print filename
		url = os.path.join(base_url, folder, filename)
		filename = os.path.join(download_folder, folder, filename)
		print '- downloading...',
		wget.download(url, filename)
		print 'done'

print 'RANDOM NUMBER FILES...'
for i in range(1, 61):
	url = base_url + 'bits.' + str(i).zfill(2)
	filename = os.path.join('bits.' + str(i).zfill(2))
	download('', filename)

print 'OTHER RANDOM NUMBER FILES...'
other_files = [ 'calif.bit', 'canada.bit', 'cdrom.doc', 'die.c', 'germany.bit' ]
download('', other_files)

print 'DOS...'
dos_files = [ 'asc2bin.exe', 'diehard.doc', 'diehard.exe', 'diequick.exe', 
			  'dosxmfsf.exe', 'getrnor.exe', 'make.txt', 'makewhat.exe', 
			  'meld.exe', 'operm5d.ata', 'tests.txt' ]
download('dos', dos_files)

print 'LINUX...'
linux_files = [ 'asc2bin', 'diehard', 'diehard.doc', 'diequick', 'getrnor', 
				'makef.txt', 'makewhat', 'meld', 'operm5d.ata', 'tests.txt' ]
download('linux', linux_files)

print 'SUN FILES...'
sun_files = [ 'asc2bin', 'diehard', 'diehard.doc', 'diequick', 'getnor', 
			  'makef.txt', 'makewhat', 'meld', 'operm5d.ata', 'test.txt' ]
download('sun', sun_files)

print 'POSTSCRIPT FILES...'
pscript_files = [ 'cdmake.ps', 'keynote.ps', 'monkey.ps', 'mwc1.ps' ]
download('pscript', pscript_files)

print '\n' + 'ALL DONE!'

