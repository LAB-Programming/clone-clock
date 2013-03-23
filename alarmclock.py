from Tkinter import *
import tkFont
from threading import Thread
import threading
import re
import time

#http://effbot.org/tkinterbook/label.htm
#http://www.saltycrane.com/blog/2008/09/simplistic-python-thread-example/


def alarm():

    
    
    for i in range(4):
        print "BEEP!!"

def addalarm():


    def alarmcount():

        coutdownhours = int(hours.get())
        countdownminets = int(minets.get())

        if pmam.get() == 'pm':

            coutdownhours = coutdownhours +  12
            

        localtime = time.asctime( time.localtime(time.time()) )
        timeHours = int(localtime[11:13])
        timeMinets = int(localtime[14:16])

        coutdownhours = coutdownhours - timeHours
        countdownminets = countdownminets - timeMinets

        global timertime
        
        timertime = coutdownhours*3600+ countdownminets*60

        foobar = threading.Timer(timertime, alarm)
        foobar.start()
        
    def newalarm():

        toplev.destroy()
        
        allarm = Frame(body, height=50, width = 300, bg = "gray") #alarm GUI
        allarm.pack(fill=X, pady=3)

        timeoff = hours.get() + ":" + minets.get(), pmam.get()
        
        label = Label(allarm, text=timeoff, bg = "gray")
        label.pack(side=LEFT, pady=10, padx = 5)

        enable = Checkbutton(allarm, bg = "gray", command = alarmcount)
        enable.pack(side=RIGHT, padx=20, pady=10)
        
    toplev = Toplevel() #adding a new alarm sepret window
    toplev.title("new alarm")
    toplev.geometry("230x150")

    dropdown = Frame(toplev, width=115)
    dropdown.pack()

    global hours
    hours = StringVar()
    hourstime = OptionMenu(dropdown, hours, '1', '2', '3','4','5','6','7','8',
                           '9','10','11','12')
    hourstime.pack(side=LEFT)

    spliter = Label(dropdown, text=" : ")
    spliter.pack(side=LEFT)

    global minets
    minets = StringVar()
    minetstime = OptionMenu(dropdown, minets, '1','2','3','4','5','6','7','8'
                            ,'9','10','11','12','13','14','15','16','17','18',
                            '19','20','21','22','23','24','25','26','27','28',
                            '29','30','31','32','33','34','35','36','37','38',
                            '39','40','41','42','43','44','45','46','47','48',
                            '49','50','51','52','53','54','55','56','57','58',
                            '59')
    minetstime.pack(side=LEFT)

    global pmam
    pmam = StringVar()
    ampm = OptionMenu(dropdown, pmam, 'am', 'pm',)
    ampm.pack(side=LEFT)
    
    okbutton = Button(toplev, text="submit", command=newalarm)
    okbutton.pack(side=BOTTOM)


    
    
def gettime():
    
        
    localtime = time.asctime( time.localtime(time.time()) )
    timeHours = int(localtime[11:13])
    timeminets = int(localtime[14:16])
    pmam = "am"
    
    if timeHours > 12:

        timeHours = timeHours - 12
        pmam = "pm"

    if timeminets > 59:

        timeHours = timeHours - 1
        timeminets = timeminets - 60

        
    global fulltime
    fulltime = (str(timeHours) + ":" + str(timeminets) + " " + pmam)
    return fulltime

def refreshnow():

    global fulltimenow
    
    while True:#runs infendnly
        
        fulltimenow = gettime()
        newtime.set(fulltimenow)
        time.sleep(2)

    

    

root = Tk()
root.title("Clock")
root.geometry("300x400")

newtime = StringVar()

t = Thread(target = refreshnow)
t.start()

top = Frame(root)
top.pack(side=TOP, fill = X)

timenow = Label(top,  textvariable = newtime, font=("verdana",20))
timenow.pack()

body = Frame(root)
body.pack(fill = X)

bot = Frame(root)
bot.pack(side=BOTTOM, fill=X)

add = Button(bot, text="+", width=1, command=addalarm)
add.pack(side=LEFT, padx=4)

root.mainloop()

