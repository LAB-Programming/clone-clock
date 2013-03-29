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
        print "BEEP!!!!!!!!"

#creates of an alarm
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
    toplev.geometry("260x150")
    root.resizable(FALSE,FALSE)

    dropdown = Frame(toplev, width=115)
    dropdown.pack(pady=10)

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
                            '59', '00')
    minetstime.pack(side=LEFT)

    global pmam
    pmam = StringVar()
    ampm = OptionMenu(dropdown,pmam, 'am', 'pm',)
    ampm.pack(side=LEFT)
    
    okbutton = Button(toplev, text="submit", command=newalarm)
    okbutton.pack(side=BOTTOM)

def addtimer():

    def newtimer():

        settimer.distory()
        

    settimer = Toplevel()
    settimer.title("new timer")
    settimer.geometry("260x150")
    root.resizable(FALSE,FALSE)

    dropdown = Frame(settimer)
    dropdown.pack(pady=10)

    mintill = StringVar()
    mintime = OptionMenu(dropdown, mintill, '01','02','03','04','05','06','07','08',
                            '09','10','11','12','13','14','15','16','17','18',
                            '19','20','21','22','23','24','25','26','27','28',
                            '29','30','31','32','33','34','35','36','37','38',
                            '39','40','41','42','43','44','45','46','47','48',
                            '49','50','51','52','53','54','55','56','57','58',
                            '59','00')
    mintime.pack(side=LEFT)
    
    sectill = StringVar()
    sectime = OptionMenu(dropdown, sectill, '01','02','03','04','05','06','07','08',
                            '09','10','11','12','13','14','15','16','17','18',
                            '19','20','21','22','23','24','25','26','27','28',
                            '29','30','31','32','33','34','35','36','37','38',
                            '39','40','41','42','43','44','45','46','47','48',
                            '49','50','51','52','53','54','55','56','57','58',
                            '59','00')
    sectime.pack(side=LEFT)
    
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
root.resizable(FALSE,FALSE)

newtime = StringVar()

t = Thread(target = refreshnow)
t.start()

top = Frame(root)
top.pack(side=TOP, fill = X)

timenow = Label(top,  textvariable = newtime, font=("verdana",20))
timenow.pack()

body = Frame(root)
body.pack(fill=X)

bot = Frame(root)
bot.pack(side=BOTTOM, fill=X)

add = Button(bot, text="alarm", width=4, command=addalarm)
add.pack(side=LEFT, padx=4)

addtimmer = Button(bot, text="timer", width=4, command=addtimer)
addtimmer.pack(side=LEFT, padx=4)
root.mainloop()

