import requests
import time
import csv
import codecs
from bs4 import BeautifulSoup


def main():
    url = "http://search.dangdang.com/?key=python&act=input&show=big&page_index="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    
    index = 1
    while index < 2:
      url = url + str(index)
      res = requests.get(url, headers)
      index = index + 1
      paraseHtml(res)

      time.sleep(1)

    copyIntoFile()


def paraseHtml(response):
   dom = BeautifulSoup(response.content, fromEncoding="gb18030")
   temps = dom.find_all('a', class_="pic")
   print(temps)
   global books
   books = books + temps
   print('当前的页面', str(len(books)))

def copyIntoFile():
  fileName = 'jdfile.csv'

  with codecs.open(fileName, 'w', 'utf_8_sig') as csvfile:
    fileNames = ['书名', '页面地址', '图片地址']
    wirter = csv.DictWriter(csvfile, fileNames)
    wirter.writeheader()

    for book in books:
      print(book.attrs['title'])
      if len(list(book.children)[0].attrs) == 3:
          img = list(book.children)[0].attrs['data-original']
      else:
          img = list(book.children)[0].attrs['src']
      try:
        wirter.writerow({'书名':book.attrs['title'], '页面地址':book.attrs['href'], '图片地址': img})
      except UnicodeEncodeError:
        print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

  print('将数据写到 ' + fileName + '成功！')



if __name__ == '__main__':
  books = []
  main()