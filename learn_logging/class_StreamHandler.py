#!encoding=utf-8

from logging import StreamHandler
from logging import LogRecord
import sys
onelog=LogRecord('name','10',pathname=__file__,lineno=10,msg=u'haha哈',args=None,exc_info=None,func=None)

S=StreamHandler(stream=sys.stdout)

S.emit(onelog)
