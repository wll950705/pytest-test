import os
'''写一个文件，接受一个参数，如果是文件，就执行这个文件，如果是文件夹，就执行这个文件夹下所有的py文件'''
def func(path):
     #先判断这个path是文件还是文件夹，isdir  isfile
     #如果是文件并且以.py结尾的
    if os.path.isfile(path) and path.endswith('.py'):
        #执行这个文件
        os.system('python %s'%path)  #模拟了在cmd中执行代码的过程
    elif os.path.isdir(path):
        #查看这个文件夹下的所有内容listdir
        for name in os.listdir(path):
            abs_path = os.path.join(path,name)
            if abs_path.endswith('.py'):
                os.system('python %s'%abs_path)
                