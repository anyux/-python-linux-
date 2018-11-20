'''
  shell的优点在于管道.管道可以将多个简单命令组合实现复杂的功能.
  在python标准库sys库中,有三个文件描述符,stdin,stdout,stderr,分别对应于标准输入,标准输出,错误输出.不需要调用open()函数打开文件就可以直接使用.例如,有一个名为read_stdin.py的文件,它仅从标准输入中读取内容,然后打印到屏幕,示例如下:
'''
from __future__ import print_function

import sys

#for line in sys.stdin:
#  print(line, end='')

'''
运行结果为:
[root@python part3]# cat /etc/hosts | python 3.1.2使用sys.stdin和fileinput读取标准输入.py 
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
'''
'''
sys.stdin是一个普通文件对象,除了对标准输入读取内容,也可以使用sys.stdin调用文件对象方法.如调用read()函数读取标准输入中的内容,调用readlines()函数将标准输入读取到一个列表中.如下所示:
'''

#def get_content():
#  return sys.stdin.readlines()
#print(get_content())

'''
运行结果为:
[root@python part3]# cat /etc/hosts | python 3.1.2使用sys.stdin和fileinput读取标准输入.py 
['127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4\n', '::1         localhost localhost.localdomain
localhost6 localhost6.localdomain6\n']
'''

'''
  awk是Linux下一个广泛使用的工具,有了sys.stdin,几乎可以不用awk.1是python与linux管道结合较好,2是python比awk使用广泛,可读性好,功能强,语法清晰.完全可以使用python代替awk处理数据
  如果熟悉awk,了解awk支持多文件处理.python使用fileinput对多文件处理.fileinput是python的标准库,fileinput可以依次读取命令行参数中的多个文件.即fileinput会遍历sys.arg[1:]列表,并读取文件内容.如果列表为空,则读取标准输入.
  一般直接调用fileinput下的input方法,按行读取内容.如,一个read_from_fileinput.py文件,在这个文件中,先导入fileinput模块,然后使用for循环遍历文件内容.如下所示:
'''
import fileinput
for line in fileinput.input():
  print(line, end="")
'''
运行结果为:
# python 3.1.2使用sys.stdin和fileinput读取标准输入.py
/etc/hosts /etc/hostname 
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
python
'''
'''
fileinput读取内容比sys.stdin更加灵活.fileinput既可以从标准输入中读取内容,也可以从文件中读取内容.如下所示:
'''
#cat /etc/passwd | 
