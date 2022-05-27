import urllib.request
fp = urllib.request.urlopen(r'http://www.python.org')
print(fp.read(100))
print(fp.read(100).decode())
fp.close()
