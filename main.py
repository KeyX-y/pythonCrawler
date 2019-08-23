import requests
import time
from taskQueue import TaskQueue
from pageThread import PageThread
from copyData import CopyData

from parseHtml import ParseHtml
from config import Config

def main():
  url = Config.getUrl()
  subUrl = Config.getSubUrl()
  THREAD_SUM = Config.getThread()
  headers = Config.getHeader()
  index = 0
  totalPages = ParseHtml.getPagesTotal()
  print(totalPages)
  time.sleep(1)

  while index < totalPages:
    if index != 0:
      url = subUrl + str(index) + '.html'

    html = requests.get(url, headers)
    html.encoding = 'utf-8'
    index = index + 1

    ParseHtml.parsePageList(html)

  taskQueue = TaskQueue.getTaskQueue()

  # 开启多线程请求页面
  for i in range(THREAD_SUM):
    workthread = PageThread(taskQueue, i)
    workthread.start()
  
  while True:
    if taskQueue.empty():
        break
    else:
        pass

  if taskQueue.empty():
    time.sleep(2)
    print('请求结束')
    # 操作数据到本地文件或数据库
    CopyData.copy()

if __name__ == "__main__":
  list = []
  main()
