from queue import Queue

class TaskQueue(object):
  pagesQueue = Queue()
  moviesQueue = Queue()

  def __init__(self):
    pass

  @classmethod
  def getTaskQueue(cls):
    return cls.pagesQueue

  @classmethod
  def getMovieQueue(cls):
    return cls.moviesQueue