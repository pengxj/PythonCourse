import urllib.request
import urllib.parse
params = urllib.parse.urlencode({"wd": "SZTU"})
url = "http://www.baidu.com/s?%s" % params
fp = open('baidu.html', 'w')
with urllib.request.urlopen(url) as f:
    fp.write(f.read().decode('gbk'))

fp.close()
