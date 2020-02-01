from taskQueue import TaskQueue
from lxml import etree
from config import Config
import requests

class ParseHtml(object):

  url = Config.getUrl()
  headers = Config.getHeader()

  def __init__(self):
    pass


  @classmethod
  def getPagesTotal(cls):
    html = requests.get(cls.url, cls.headers)
    html.encoding = 'utf-8'
    content = etree.HTML(html.text)
    lastPage = content.xpath("//a[@class='last']/@href")[0]
    lastTotal = lastPage.split('_')[1][0:3]
    return int(lastTotal)

  @classmethod
  def parsePageList(cls, dom):
    taskQueue = TaskQueue.getTaskQueue()
    baseUrl = 'http://www.hkb123.com'
    content = etree.HTML(dom.text)
    con = content.xpath("//div[@class='channel-content']/ul/child::*")

    for section in con:
      aHref = section.xpath("./a/@href")[0]

      movieUrl = baseUrl + str(aHref)
      movieName = section.xpath("./p/a/text()")
      movieImg = section.xpath("./a/img/@src")[0]
      movieType = section.xpath("./p[last()]/text()")

      if not movieName:
        movieName = section.xpath("./p/a/font/text()")[0]


      movie = {
        'movieUrl': movieUrl,
        'movieName': movieName[0],
        'movieImg': movieImg,
        'movieType': movieType,
      }

      taskQueue.put(movie, 3)