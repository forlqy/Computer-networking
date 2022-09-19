import sys #与Python解释器及其环境操作相关的标准库
import time #与时间相关各种函数库
print(sys.getsizeof(22)) #占用内存大小
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())
