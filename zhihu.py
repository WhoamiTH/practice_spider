# coding=utf-8

import urllib.request
import re
import http.cookiejar
from bs4 import BeautifulSoup
import os
'''
page = 1
root_url = 'https://www.zhihu.com/collection/52598162?page=' + str(page)
xsrf = '0019a34eccfe90165a44cdff664fb51f'
User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
Referer = "https://www.zhihu.com/"
headers={
    'User-Agent' : User_Agent,
    'Referer' : Referer
}
#抓url
request = urllib.request.Request(root_url)
response = opener.open(request)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content,'html.parser')
url_tems = soup.find_all('a', class_="toggle-expand")
urls_set = set()
for url in url_tems:
    full_url = urllib.request.urljoin('https://www.zhihu.com', url.get('href'))
    urls_set.add(full_url)
    print(full_url)
'''
'''
#抓photo
test_url ='https://www.zhihu.com/question/46458423/answer/139116592'
request = urllib.request.Request(test_url)
response = opener.open(request)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content,'html.parser')
image_url = set()
image_url_tem = soup.find_all('img',class_="origin_image zh-lightbox-thumb lazy")
for url_tem in image_url_tem :
    image_url.add(url_tem.get('data-original'))
'''
class mybeautySpider():

    def __init__(self):
        self.page = 1
        self.max_page = 1
        User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
        Referer = "https://www.zhihu.com/collection/52598162"
        self.headers = {
            'User-Agent': User_Agent,
            'Referer': Referer
        }
        self.cookie = http.cookiejar.CookieJar()
        self.handler = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.handler)
        self.exam =set()
        self.urls_set = set()
        self.image_urls = set()
        op = urllib.request.build_opener()

    def getMaxUrl(self,target_url):
        request = urllib.request.Request(target_url)
        # response = self.opener.open(request)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        # content = urllib.request.urlopen(target_url).read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        page_soup = soup.find_all('a',href = re.compile(r'\?page=\d+'))
        page_digit = set()
        for page in page_soup:
            test = page.get_text()
            if test.isdigit():
                page_digit.add(int(test))
        self.max_page =int(max(page_digit))


    def getUrl(self,target_url):
        request = urllib.request.Request(target_url,headers=self.headers)
        response = self.opener.open(request)
        content = response.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        url_tems = soup.find_all('a', class_="toggle-expand")
        print(url_tems)
        for url in url_tems:
            full_url = urllib.request.urljoin('https://www.zhihu.com', url.get('href'))
            self.urls_set.add(full_url)



    def getOneUrl(self):
        url = self.urls_set.pop()
        return url

    def getPicUrl(self,target_url):
        request = urllib.request.Request(target_url,headers=self.headers)
        response = self.opener.open(request)
        content = response.read().decode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        image_url_tem = soup.find_all('img', class_="origin_image zh-lightbox-thumb lazy")
        for url_tem in image_url_tem:
            self.image_urls.add(url_tem.get('data-original'))


    def downloadPic(self):
        count = 1
        path = os.getcwd()
        os.makedirs(str(path)+'\\beauty')
        for url in self.image_urls :
            try:
                urllib.request.urlretrieve(url,str(path)+'\\beauty\\{0}.png'.format(count))
            except:
                print("链接失效")
            print("正在下载第{0}张图片".format(count))
            count = count +1
        print("已经下载完毕,共下载{0}张图片".format(count))
        print("Enjoy it!")

    def start(self,url):
        self.getMaxUrl(root)
        page_count = 1
        while True:
            rootUrl = root + "?page=" + str(self.page)
            print("开始抓取第{0}页".format(page_count))
            self.getUrl(rootUrl)
            self.page += 1
            page_count += 1
            if self.page > self.max_page:
                url_num = len(self.urls_set)
                print("共抓取成功{0}条链接".format(url_num))
                break

        print("收藏夹答案链接抓取完毕，开始抓取链接图片")
        count_imgurl = 1
        for url in self.urls_set:
            try:
                self.getPicUrl(url)
            except:
                print("失效一个")
            print("正在抓取第{0}个链接图片".format(count_imgurl))
            count_imgurl += 1
        print("共抓取到{0}个图片".format(len(self.image_urls)))
        print("图片链接全部抓取完毕，开始下载图片")
        self.downloadPic()

if __name__ == '__main__':
    # root = input("请输入想要下载的收藏夹地址：")
    # if root == '':
    #     root = "https://www.zhihu.com/collection/52598162"
    root = "https://www.zhihu.com/collection/30649557"
    abc = mybeautySpider()
    abc.getUrl(root)