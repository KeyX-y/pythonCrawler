
class Config(object):
  url = 'http://www.hkb123.com/dongzuopian/index.html'
  subUrl = 'http://www.hkb123.com/dongzuopian/index_'
  THREAD_SUM = 6
  movieType = ['dongzuopian', 'xijupian', 'aiqingpian', 'kehuanpian', 'kongbupian', 'zhanzhengpian', 'juqingpian','m_jlp', 'donghuapian', 'gaoqing']

  @classmethod
  def getHeader(cls):
    return {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
  }

  @classmethod
  def getUrl(cls):
    return cls.url

  @classmethod
  def getMovieType(cls):
    return cls.movieType

  @classmethod
  def getSubUrl(cls):
    return cls.subUrl

  @classmethod
  def getThread(cls):
    return cls.THREAD_SUM