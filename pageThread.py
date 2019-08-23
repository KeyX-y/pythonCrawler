import threading
import requests
import time
from lxml import etree
from config import Config
from taskQueue import TaskQueue

class PageThread(threading.Thread):
  NOT_EXIST = 0
  movieQueue = TaskQueue.getMovieQueue()

  def __init__(self, queue, id):
    threading.Thread.__init__(self)
    self.queue = queue
    self.id = id

  def run(self):
    while not self.NOT_EXIST:
      if self.queue.empty():
          self.NOT_EXIST = 1
          self.queue.task_done()
          break

      currentMovie = self.queue.get()
      url = currentMovie['movieUrl']
      headers = Config.getHeader()

      try:
        response = requests.get(url, headers=headers, timeout=3)
        print('Task 子线程 ' + str(self.id) + ' 请求【 ' + url + ' 】的结果：' + str(response.status_code))
        response.encoding = 'utf-8'

        if response.status_code != 200:
          self.queue.put(currentMovie)
          time.sleep(20)
        else :
          content = etree.HTML(response.text)
          movieName = content.xpath("//div[@class='intro']/h2/text()")[0]
          downList = []
          con = content.xpath("//div[@class='baiduyunaddres']/ul/child::*")
          
          for section in con:
            aHref = section.xpath("./a/@href")[0]
            name = section.xpath("./a/text()")[0]

            movie = {
              'name': name,
              'downUrl': aHref
            }

            downList = downList + [movie]
          
        currentMovie = {
          'movieName': movieName,
          'list': downList
        }

        self.movieQueue.put(currentMovie, 3)

      except Exception as e:
        print(e)
