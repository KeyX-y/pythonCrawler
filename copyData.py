from taskQueue import TaskQueue
import codecs
import csv

class CopyData(object):
  NOT_EXIST = 0

  def __init__(self):
    pass

  @classmethod
  def copy(self):
    movieQueue = TaskQueue.getMovieQueue()
    fileName = 'data.csv'
    print(movieQueue.qsize())

    with codecs.open(fileName, 'a+' ,encoding='utf_8_sig') as f:
      filednames = ['电影名称', '下载地址']
      writer = csv.DictWriter(f,filednames)
      writer.writeheader()

      while not self.NOT_EXIST:
        if movieQueue.empty():
            self.NOT_EXIST = 1
            movieQueue.task_done()
            break

        currentMovie = movieQueue.get()

        writer.writerow({filednames[0]: currentMovie['movieName'], filednames[1]: currentMovie['list']})
