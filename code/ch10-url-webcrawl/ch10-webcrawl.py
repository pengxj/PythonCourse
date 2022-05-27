import requests
from bs4 import BeautifulSoup
import time
import pdb

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
url = 'https://bdi.sztu.edu.cn/xyjj/jzyg1/jytd/fjs.htm'
domain = 'https://bdi.sztu.edu.cn'
 
resp = requests.get(url, headers)
resp.encoding = 'utf-8'
# print(resp.text)
 
# 把网页源代码传给bs
page = BeautifulSoup(resp.text, 'lxml')
a_list = page.find_all('img')  #.find_all('a') , class_='TypeList'html.parser

pdb.set_trace()
for al in a_list:
    # 使用get可以直接拿到属性值
    src = domain + al.get('src')  
    print(src)  
    src = src.split('?')[0]
    if 'local' in src:
        # 下载图片
        img_resp = requests.get(src)
        # 这里拿到的是字节
        # img_resp.content
        img_name = src.split('/')[-1]
        with open('img/' + img_name, mode='wb') as f:
            f.write(img_resp.content)
        f.close()
        print('Pic:{} download successfully!'.format(img_name))
        time.sleep(1)
resp.close()
print('All Over!')