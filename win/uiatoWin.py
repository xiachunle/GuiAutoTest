# -*- coding:utf-8 -*-
import  subprocess
from uiautomation import *
import  logging
import  psutil

import time
def  setTime():
    return  time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime())


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fn = logging.FileHandler('hq.log',mode='w')

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fn.setFormatter(formatter)
logger.addHandler(fn)
def  startApp(path):
    try:
        subprocess.Popen(path)
        return True
    except:
        logger.error(" %s not found"%str(path))
        return False



#获取运行程序的内存
def getMemCpu(name):
    pids = psutil.pids()
    line = ""
    for pid in pids:
        p = psutil.Process(pid)

        if p.name() == name:
            line = format("%s_mem:%s" % (p.name(), psutil.Process(pid).memory_info().rss))
    logger.info("=============")
    logger.info(line)
    logger.info("=============")


def  getWindowTitle(titlename):
    levelWindow = WindowControl(searchDepth=1, ClassName='Qt5QWindowIcon', Name=titlename)
    if (levelWindow.Exists()):
        # logger.info('测试窗口标题为%s'))
        levelWindow.SetTopmost(True)
        return levelWindow
    else:
        # logger.error('%s窗口名称未找到'%titlename)
        return False

#打开行情管理和用户管理 tielename
def openManager(titlename,name,itemName):
    if(titlename == 'Level2-Server' or titlename == 'Level2-Client'):
        levelWindow=getWindowTitle(titlename)
        if(levelWindow is not False):
            if (name == u'配置'):
                c = MenuItemControl(searchFromControl=levelWindow, Name=u'配置')
                c.Click()
                configWindow = MenuControl(searchFromControl="", LocalizedControlType=u'菜单')
                if (itemName == u'行情代理' or itemName == u'用户管理'):
                    configWindow.MenuItemControl(searchDepth=1, Name=itemName).Click()
                    return True
                else:
                    logger.error("%s 功能项未发现" % str(itemName))
                    return False
            elif (name == u'帮助'):
                logger.info("帮助菜单暂无测试内容")
                return False
            else:
                logger.error("%s 菜单栏未发现内容" % str(name))
                return False
    else:
        logger.error("暂未支持该应用或应用程序标题名不对:%s"%str(titlename))
        return False



#行情管理
def hqConfig():

    hqWindow=getWindowTitle(u'行情代理')
    print(hqWindow)
    buttonIndex=1
    button=ButtonControl(searchFromControl=hqWindow,foundIndex=buttonIndex,LocalizedControlType=u"按钮")
    while(button.Exists()):
            button.MoveCursorToMyCenter()
            print(button)
            buttonIndex+=1
            button = ButtonControl(searchFromControl=hqWindow, foundIndex=buttonIndex, LocalizedControlType=u"按钮")

    add1=ButtonControl(searchFromControl=hqWindow, foundIndex=3, LocalizedControlType=u"按钮")
    add1.MoveCursorToMyCenter()
    add1.Click()

#用户管理
def userConfig():
   pass


if __name__ == '__main__':
    startApp('D:\hqzf\L2Sever\Monitor\Level2Sever.exe')
    getMemCpu('Level2Server.exe')
    count = 0
    while (True):
        openManager(u'Level2-Server', u'配置', u'行情代理')
        hqConfig()
        getMemCpu('Level2Server.exe')
        count += 1
        time.sleep(5)
        logger.info(format('已循环多少次%s' % str(count)))


