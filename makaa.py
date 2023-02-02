import os
import sys
import time
import psutil
import _thread
import colorama
import webbrowser
import tkinter as tk
import urllib.request

VER = '0.1.1 Beta'

# 
#   Copyright (c) 2022-2023 BlocksTeam 
#   Makaa Server Launch
#

print(colorama.Fore.RED + '[Makaa Server Launch Version: ' + VER + ']' )



class GetFile:

    def __init__(self, file_type=''):

        # file_type should be string
        if isinstance(file_type, str):
            self.file_type = file_type.lower()
        else:
            self.file_type = ''

        # initial return list
        self.short_name = []
        self.full_name = []

    def _filter(self, _file_type):
        """ 
        : if import file type is blank, return all items.
        : if import file type is not blank, return special item.
        """

        if self.file_type != '':
            if _file_type == self.file_type:
                return True
            else:
                return False
        else:
            return True

    def get(self, fold_address):
        """find item in fold"""

        for fl in os.listdir(fold_address):
            new_dir = os.path.join(fold_address, fl)

            if os.path.isfile(new_dir) and self._filter(fl[-len(self.file_type):]):
                # find full name
                self.full_name.append(os.path.abspath(new_dir))
                # find short name
                self.short_name.append(fl)
                # self.short_name.append(fl[:-(len(self.file_type) + 1)])

            elif os.path.isdir(new_dir):
                self.get(new_dir)

        return self.short_name, self.full_name

def makeServer(startmem,serverFile):
    os.system('java -Xmx' + str(startmem) + 'm java -server -Xincgc -Xss512K -XX:+AggressiveOpts -XX:+UseCompressedOops -XX:+UseCMSCompactAtFullCollection -XX:+UseFastAccessorMethods -XX:ParallelGCThreads=4 -XX:+UseConcMarkSweepGC -XX:CMSFullGCsBeforeCompaction=2 -XX:CMSInitiatingOccupancyFraction=70 -XX:-DisableExplicitGC -XX:TargetSurvivorRatio=90 -jar ' + serverFile)

def findJarFile():
    address = os.getcwd() + '/server'
    m, n    = GetFile('jar').get(address)
    print('Jar文件被吃掉了!找到了一些幸存的Jar文件,列表如下,请输入使用的名称.')
    print(str(m))
    del n
    return 'startInputSelf'

class MakaaServer:
    def __init__(self,serverFile='',make=False,autoRestart=False):
        self.serverFile  = serverFile
        self.make        = make
        self.autoRestart = autoRestart
        if serverFile == '':
            stauts = findJarFile()
            if stauts != '':
                self.serverFile = input('请输入Jar文件名:')
            else:
                print("致命错误!(Makaa Server Error: Server File Not Found[E000])")
    
    def startServer(self):
        """Start Makaa Minecraft Server"""
        nowTime = str(int(time.time()))
        uuid    = str(uuid.uuid4()) + str(nowTime)
        del nowTime
        if self.make:
            with open('makaaCofing','w') as f:
                f.write(self.serverFile + ',' + self.autoRestart + ',' + uuid )
        else:
            with open('makaaCofing','r') as f:
                cofing = f.read()
            cofing = cofing.split(',')
        if cofing[0] != self.serverFile:
            print('ServerFile走丢了!如果这不是个意外,请将make设为True(Makaa OS:谋杀犯!')
        else:
            if cofing[1] == 'True':
                reStart = True
            else:
                reStart = False
            mem    = psutil.virtual_memory()
            canmem = float(mem.free) / 1024 / 1024 / 1024
            if canmem > 2:
                startmem = 2048
            elif canmem > 1:
                startmem = 1024
            else:
                startmem = 512
            try:
                while True:
                    makeServer(startmem,self.serverFile)
            except:
                print(colorama.Fore.CYAN + 'Makaa 已关闭' )
    def stopServer(self):
        """Stop Makaa Minecraft Server"""
        os.system('taskkill /F /IM java.exe')
        os.system('taskkill /F /IM javaw.exe')

def startServer():
    try:
        server = MakaaServer()
    except:
        print('出错了!QwQ Makaa Server 未知错误')
def command(threadname):
    print('[Makaa Server] Makaa 命令行模式 Thread %s' % threadname)
    while True:
        command = input('Python command: ')
        run = exec(command)
        print(run)
def startCommand():
    _thread.start_new_thread(command, ("Thread-1",) )
def newCofing():
    os.system('notepad /server/server.properties')
def rmTemp():
    try:
        os.remove('wall.jpg')
    except FileNotFoundError:
        pass
    sys.exit(0)
if __name__ == '__main__':
    picurl = 'https://i.328888.xyz/2023/02/02/IRccv.gif'
    f = urllib.request.urlopen(picurl)
    data = f.read()
    with open("IRccv.gif", "wb") as code:
        code.write(data)
    #判断是否安装Java
    if(not os.system('java')):
        print(colorama.Fore.RED + '正在下载Java Please Wait!')
        if 'win' in sys.platform:
            downloadUrl = 'https://www.onlinedown.net/iopdfbhjl/10044859?module=download&t=website'
            #对不起Windows用户 我只能送你到这一步了
            webbrowser.open(downloadUrl)
            sys.exit()
        else:
            print('Linux不支持自动安装Python!')
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    window = tk.Tk()
    window.title('Makaa Server Launch')
    window.geometry('850x500')
    photo = tk.PhotoImage(file="IRccv.gif")
    w = tk.Label(window, image=photo)
    l1 = tk.Label(window, text='Makaa Server Launch Version ' + VER + ' QAQ[Tips] Makaa 会自动寻找Jar文件',  font=('Arial', 12), width=80, height=2)
    b1 = tk.Button(window, text='启动服务器', width=10, height=1, command=startServer)
    b2 = tk.Button(window, text='修改配置文件', width=10, height=1, command=newCofing)
    b3 = tk.Button(window, text='命令行模式', width=10, height=1, command=startCommand)
    b4 = tk.Button(window, text='退出', width=10, height=1, command=rmTemp)
    l1.pack()
    b2.pack()
    b3.pack()
    b1.pack()
    w.pack()
    window.mainloop()