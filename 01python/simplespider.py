import re
import urllib.request

def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(request)
    html = page.read()
    print(html.decode("UTF-8"))
    return html.decode("UTF-8")


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'

    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

def down(list):
    n = 1
    for imageurl in list:
        print("正在下载第%d张图片"%n)
        conn = urllib.request.urlopen(imageurl)
        f = open("spider/"+str(n)+".jpg", 'wb')
        f.write(conn.read())
        n = n+1


html = getHtml("http://tieba.baidu.com/p/2460150866")
downlist = getImg(html)
print(downlist)
down(downlist)
