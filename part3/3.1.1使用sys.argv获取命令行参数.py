'''
  编写Linux下的命令行工具,很时候都需要解析命令行参数.如果参数简单,可以不使用解析参数的库,直接访问命令行参数.在Python中,sys库下有一个名为argv的列表,它保存了所有命令行参数.argv列表中的第一个元素是程序名称,其他的参数会以字符串的形式保存在列表中.
  例如,有一个名为test_argv.py的文件,仅导入sys,使用print函数打印argv列表内容.test_argv.py文件内容如下:
    注:此处为方便,运行当前文件
'''
from __future__ import print_function
import sys

print(sys.argv)


'''
运行结果为:

# python 3.1.1使用sys.argv获取命令行参数.py 
['3.1.1使用sys.argv获取命令行参数.py']
# python 3.1.1使用sys.argv获取命令行参数.py localhost 3306
['3.1.1使用sys.argv获取命令行参数.py', 'localhost', '3306']

'''
'''
sys.argv是一个保存命令行参数的普通列表.可以修改它,以下为应用场景:
'''
# 提示已引入print_function模块,此处不再重复引入
#from __future__ import print_function
import os
import sys

def main():
  sys.argv.append("")
  filename = sys.argv[1]
  if not os.path.isfile(filename):
    raise SystemExit(filename + 'does not exists')
  elif not os.access(filename,os.R_OK):
    raise SystemExit(filename + 'is not accessible')
  else:
    print(filename + 'is accessible')

if __name__ == '__main__':
  main()

'''
运行结果为:
# python 3.1.1使用sys.argv获取命令行参数.py /etc/hosts
['3.1.1使用sys.argv获取命令行参数.py', '/etc/hosts']
/etc/hostsis accessible
'''
'''
分析:
  在这个例子中,我们从命令行参数获取文件的名称,然后判断文件是否存在.不存在则给出提示,否则,使用os.access判断对文件的读权限.我们通过
sys.argv[1]获取文件名称.这里为避免出现异常,向argv追加一个空字符串元素,防止用户没有输入参数显示异常


'''
