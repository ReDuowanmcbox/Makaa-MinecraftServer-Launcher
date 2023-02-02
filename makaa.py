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
#   Makaa Server Launch
#

print(colorama.Fore.RED + '[Makaa Server Launch Version: ' + VER + ']' )

langs = [
'Jar文件被吃掉了!找到了一些幸存的Jar文件,列表如下,请输入使用的名称.','致命错误!(Makaa Server Error: Server File Not Found[E000])',
'ServerFile走丢了!如果这不是个意外,请将make设为True(Makaa OS:谋杀犯!','出错了!QwQ Makaa Server 未知错误',
'[Makaa Server] Makaa 命令行模式 线程:','启动服务器',
'修改配置文件','命令行模式','退出'
]

def getText(lang, num):
    return langs[num]
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
    print(getText('zh_CN',0))
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
                self.serverFile = input('fileName:')
            else:
                print(getText('zh_CN',1))
    
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
            print(getText('zh_CN',2))
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
                print(colorama.Fore.CYAN + 'Makaa Exit' )
    def stopServer(self):
        """Stop Makaa Minecraft Server"""
        os.system('taskkill /F /IM java.exe')
        os.system('taskkill /F /IM javaw.exe')

def startServer():
    try:
        server = MakaaServer()
    except:
        print(getText('zh_CN',3))
def command(threadname):
    print(colorama.Fore.CYAN + getText('zh_CN',4) + threadname)
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
def toEN():
    langs = [
    'Jar file does not exist, please select one.','Makaa Server Error: Server File Not Found[E000]',
    'ServerFile does not exist! If this is not an accident, you can set the make property of the class to True in command mode',
    'Makaa Server Unkown Error ,Lmao','[Makaa Server] Makaa Command Mode Thread:',
    'Start Server','New properties','Command Mode','Exit']
if __name__ == '__main__':
    try:
        if sys.argv[1] == 'command':
            if sys.argv[2] == 'en':
                toEN()
            startCommand()
        if sys.argv[1] == 'en':
            toEN()
    except:
        pass
    picurl = 'https://i.328888.xyz/2023/02/02/IRccv.gif'
    f = urllib.request.urlopen(picurl)
    data = f.read()
    with open("IRccv.gif", "wb") as code:
        code.write(data)
    #判断是否安装Java
    if(not os.system('java')):
        print(colorama.Fore.RED + 'Download Java Please Wait!')
        if 'win' in sys.platform:
            downloadUrl = 'https://www.onlinedown.net/iopdfbhjl/10044859?module=download&t=website'
            #对不起Windows用户 我只能送你到这一步了
            webbrowser.open(downloadUrl)
            sys.exit()
        else:
            print('Please Download Java!')
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    window = tk.Tk()
    window.title('Makaa Server Launch')
    window.geometry('850x500')
    photo = tk.PhotoImage(file="IRccv.gif")
    w = tk.Label(window, image=photo)
    l1 = tk.Label(window, text='Makaa Server Launch Version ' + VER + ' QAQ',  font=('Arial', 12), width=80, height=2)
    b1 = tk.Button(window, text=getText('zh_CN',5), width=10, height=1, command=startServer)
    b2 = tk.Button(window, text=getText('zh_CN',6), width=10, height=1, command=newCofing)
    b3 = tk.Button(window, text=getText('zh_CN',7), width=10, height=1, command=startCommand)
    b4 = tk.Button(window, text=getText('zh_CN',8), width=10, height=1, command=rmTemp)
    l1.pack()
    b2.pack()
    b3.pack()
    b1.pack()
    w.pack()
    window.mainloop()