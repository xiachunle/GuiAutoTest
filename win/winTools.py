# coding=utf-8
import psutil

import time
def  setTime():

    return  time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime())
def getMemCpu():
    data=psutil.virtual_memory()
    total = data.total  # 总内存,单位为byte
    free = data.available  # 内存
    memory = "Memory usage:%d" % (int(round(data.percent))) + "%" + total
    cpu = "CPU:%0.2f" % psutil.cpu_percent(interval=1) + "%"+free
    return memory + cpu

def main():
    info = psutil.virtual_memory()

if __name__ == '__main__':
   pids= psutil.pids()
   line =""
   for pid in pids:
       p = psutil.Process(pid)

       if p.name()=='Level2Sever.exe':
         line = format("%s_mem:%s"%(setTime(),psutil.Process(pid).memory_info().rss))
   print(line)
   time.sleep(6*3600)
   for pid in pids:
       p = psutil.Process(pid)

       if p.name()=='Level2Sever.exe':
            line = format("%s_mem:%s"%(setTime(),psutil.Process(pid).memory_info().rss))

   print(line)
   time.sleep(6*3600)
   for pid in pids:
       p = psutil.Process(pid)

       if p.name() == 'Level2Sever.exe':
           line = format("%s_mem:%s" % (setTime(), psutil.Process(pid).memory_info().rss))

   print(line)
   time.sleep(6 * 3600)
   for pid in pids:
       p = psutil.Process(pid)

       if p.name() == 'Level2Sever.exe':
           line = format("%s_mem:%s" % (setTime(), psutil.Process(pid).memory_info().rss))

   print(line)
   time.sleep(6 * 3600)
