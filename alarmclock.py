from Tkinter import *
import sys
import tkFont
from threading import Thread
import threading
import re
import time

#http://effbot.org/tkinterbook/label.htm
#http://www.saltycrane.com/blog/2008/09/simplistic-python-thread-example/

####################alarm clock###############

def alarm():

    for i in range(4):
        print "BEEP!!!!!!!!"

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

    
####################stop#########################
    
def stopupdate():

    def timenow():

        fulltime = time.asctime() 
            
        hournow = int(fulltime[11:13])
        minnow = int(fulltime[14:16])
        secnow = int(fulltime[17:19])

        timeinsec = hournow*3600 + minnow*60 + secnow

        #print "timenow:", timeinsec
        return timeinsec
    
    def timeinsec():
        
        sec = timenow() - 1
        return sec

    seclabel = int(seclap.get())
    minlabel = int(minlap.get())
    
    while True:

        if timenow() == timeinsec():

            seclabel = seclabel + 1

            if seclabel > 59:

                minlabel = minlable + 1
                seclabel = 0
                
            lap.set(str(minlabel) + ":" + str(seclabel))
            

            
        
    
def addstop():

    def stopstart():

        thread3 = Thread(target = stopupdate)
        thread3.start()
        
    def stopstop():

        thread3.stop()
        
    stop = Frame(body, height=50, width = 300, bg = "gray") #timer GUI frame
    stop.pack(fill=X, pady=3)

    global minlap
    global seclap
    
    minlap = StringVar()
    minlap.set("0")
    
    seclap = StringVar()
    seclap.set("00")

    global lap
    
    lap = StringVar()
    lap.set( minlap.get() + ":" + seclap.get() )
    
    stoplabel = Label(stop, textvariable=lap, bg="gray")
    stoplabel.pack(side = LEFT, padx=20, pady=10)

    buttonstop = Button(stop, bg="gray", text="stop")
    buttonstop.pack(side=RIGHT, padx=5)

    buttonstart = Button(stop, bg="gray", text="start", command=stopstart)
    buttonstart.pack(side=RIGHT, padx=5)


######################timer######################
        
def timerupdate():# thread-2

    def timenow():

        fulltime = time.asctime() 
            
        hournow = int(fulltime[11:13])
        minnow = int(fulltime[14:16])
        secnow = int(fulltime[17:19])

        timeinsec = hournow*3600 + minnow*60 + secnow

        #print "timenow:", timeinsec
        return timeinsec
    
    def timethen():

        timetill = (int(mintill.get()) * 60) + int(sectill.get())
        timethen = starttime + timetill

        #print "timethen: ", timethen
        return timethen
        

    def timeinsec():

        timeinasec = whatsthetime + 1
        #print timeinasec
        return timeinasec
    
    global starttime
    global whatsthetime
    
    sectimetill = int(sectill.get())
    mintimetill = int(mintill.get())
    starttime = timenow()
    whatsthetime = timenow()

    endtime = timethen()

    while True:
        
        if  timenow() == endtime:

            print "beep"
            coutdown.set( mintill.get() + ":" + sectill.get() )
            sys.exit()
        
        if timenow() == timeinsec():

            sectimetill = sectimetill - 1

            if sectimetill < 0:

                mintimetill = mintimetill - 1
                sectimetill = sectimetill + 59
                
            coutdown.set( str(mintimetill) + ":" + str(sectimetill) )
            
            whatsthetime = timenow()

#creation of timer

def addtimer():

    def timercount():
        
        thread2 = Thread(target = timerupdate)
        thread2.start()

    def newtimer():

        settimer.destroy()

        timer = Frame(body, height=50, width = 300, bg = "gray") #timer GUI frame
        timer.pack(fill=X, pady=3)

        global coutdown
        
        coutdown = StringVar()
        coutdown.set( mintill.get() + ":" + sectill.get() )
        
        coutdownlabel = Label(timer, textvariable=coutdown, bg="gray")
        coutdownlabel.pack(side = LEFT, padx=20, pady=10)

        buttonstart = Button(timer, bg="gray", text="start", command=timercount)
        buttonstart.pack(side=RIGHT, padx=5)
        
        

    settimer = Toplevel()
    settimer.title("new timer")
    settimer.geometry("260x150")
    settimer.resizable(FALSE,FALSE)

    dropdown = Frame(settimer)
    dropdown.pack(pady=10)

    global mintill
    
    mintill = StringVar()
    mintime = OptionMenu(dropdown, mintill, '1','2','3','4','5','6','7','8',
                            '9','10','11','12','13','14','15','16','17','18',
                            '19','20','21','22','23','24','25','26','27','28',
                            '29','30','31','32','33','34','35','36','37','38',
                            '39','40','41','42','43','44','45','46','47','48',
                            '49','50','51','52','53','54','55','56','57','58',
                            '59','0')
    mintime.pack(side=LEFT)

    global sectill
    
    sectill = StringVar()
    sectime = OptionMenu(dropdown, sectill, '01','02','03','04','05','06','07','08',
                            '09','10','11','12','13','14','15','16','17','18',
                            '19','20','21','22','23','24','25','26','27','28',
                            '29','30','31','32','33','34','35','36','37','38',
                            '39','40','41','42','43','44','45','46','47','48',
                            '49','50','51','52','53','54','55','56','57','58',
                            '59','00')
    sectime.pack(side=LEFT)

    submitbutton = Button(settimer, text="submit", command=newtimer)
    submitbutton.pack(side=BOTTOM)
    
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
    fulltime = (str(timeHours) + ":" + ("0" if timeminets < 10 else "") + str(timeminets) + " " + pmam)
    return fulltime
    

##################clock###################

def refreshnow(): #thread-1

    global fulltimenow
    
    while True:#runs infendnly
        
        fulltimenow = gettime()
        newtime.set(fulltimenow)
        time.sleep(2)
    

##################main GUI##################

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
bot.pack(side=BOTTOM)

add = Button(bot, text="alarm", width=4, command=addalarm)
add.pack(side=LEFT, padx=4)

addtimmer = Button(bot, text="timer", width=4, command=addtimer)
addtimmer.pack(side=LEFT, padx=4)

addstop = Button(bot, text="stop", width=4, command=addstop)
addstop.pack(side=LEFT, padx=4)

root.mainloop()

