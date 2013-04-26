from Tkinter import *
from threading import Thread
import threading
import sys
import tkFont
import time

def clockupdate(): #update the time and sets a varuable

        while True:
            
            time.sleep(1)
            clock.set(timenow.string())

        
class timenow: #diffnet ways of getting the time
    
    def number(self): #returns the timein sec

        self.fulltime = time.asctime() 
                
        self.hournow = int(self.fulltime[11:13])
        self.minnow = int(self.fulltime[14:16])

        self.timeinsec = self.hournow*3600 + self.minnow*60

        return self.timeinsec

    def string(self):# if you what the time as a string

        self.timefull = time.asctime()
        self.hour = int(self.timefull[11:13])
        self.min = int(self.timefull[14:16])

        if self.hour >= 13:

            self.hour = self.hour - 12
            self.ampm = "pm"

            if self.hour == 12:

                self.ampm = "am"

        elif self.hour <= 12:

            self.hour = self.hour
            self.ampm = "am"

            if self.hour == 12:

                self.ampm = "pm"

        return str(self.hour) + ":" + ("0" if self.min < 10 else "") + str(self.min) + " " + self.ampm
        
            
class alarmclock: #containes what you need for the alarms

    def createGUI(self): #creates the GUI on the alarm on root

        def count(): #does all the math for for the time 

                self.start.configure(state=DISABLED, background='cadetblue')
                
                self.thenhours = int(self.hours.get())
                self.thenminets = int(self.minets.get())
                self.thenampm = self.pmam.get()

                if self.thenampm == "pm" and self.thenhours != 12:

                    self.thenhours = self.thenhours + 12

                self.thenhours = self.thenhours * 3600
                self.thenminets = self.thenminets * 60
                self.timetill = (self.thenminets + self.thenhours) - timenow.number()

                self.timerthread = threading.Timer(self.timetill, alarm.alarm)
                self.timerthread.start()

                ########
        

        self.config.destroy()
        
        self.alarmclock = Frame(body, bg="gray")
        self.alarmclock.pack(fill=X, pady = 5)

        self.timeframe = Frame(self.alarmclock, bg="gray")
        self.timeframe.pack(side = LEFT, padx = 3)

        self.hourslabel = Label(self.timeframe, textvariable = self.hours,
                                bg = "gray", height=3)
        self.hourslabel.pack(side=LEFT)

        self.spliterlabel = Label(self.timeframe, text = ":", bg = "gray")
        self.spliterlabel.pack(side = LEFT)
        
        self.minetslabel = Label(self.timeframe, textvariable = self.minets,
                                 bg = "gray")
        self.minetslabel.pack(side = LEFT)

        self.ampmlabel = Label(self.timeframe, textvariable = self.pmam,
                               bg = "gray")
        self.ampmlabel.pack(side = LEFT, padx = 2)
        
        self.start = Button(self.alarmclock, text = "start", command=count)
        self.start.pack(side=RIGHT, padx = 4)


        
    
    def alarm(self): # when the alarm gose this function runs (untill sound libraary is found)
        
        for self.i in range(4):

            print "beep!!"

        
    def start(self): # creates the childed window

        self.config = Toplevel()
        self.config.title("add alarm")
        self.config.geometry("260x150")
        self.config.resizable(FALSE,FALSE)

        self.dropdown = Frame(self.config)
        self.dropdown.pack(fill=Y, pady=10)

        self.hours = StringVar()
        self.hourstime = OptionMenu(self.dropdown, self.hours, '1', '2', '3','4','5','6','7','8',
                           '9','10','11','12')
        self.hourstime.pack(side=LEFT)

        self.spliter = Label(self.dropdown, text=" : ")
        self.spliter.pack(side=LEFT)

        self.minets = StringVar()
        self.minetstime = OptionMenu(self.dropdown, self.minets, '01','02','03','04','05','06','07','08'
                            ,'09','10','11','12','13','14','15','16','17','18',
                            '19','20','21','22','23','24','25','26','27','28',
                            '29','30','31','32','33','34','35','36','37','38',
                            '39','40','41','42','43','44','45','46','47','48',
                            '49','50','51','52','53','54','55','56','57','58',
                            '59', '00')
        self.minetstime.pack(side=LEFT)
        
        self.pmam = StringVar()
        self.ampm = OptionMenu(self.dropdown ,self.pmam, 'am', 'pm',)
        self.ampm.pack(side=LEFT)

        self.buttons = Frame(self.config)
        self.buttons.pack(side=BOTTOM)
        

        self.submit = Button(self.buttons, text = "submit", width = 6, command = alarm.createGUI)
        self.submit.pack(side=LEFT, padx = 2)

        self.done = Button(self.buttons, text = "cancel" , width = 6, command = self.config.destroy)
        self.done.pack(side = LEFT, padx = 2)

        

####GUI#####

root = Tk()
root.title("clock")
root.geometry("300x400")
root.resizable(FALSE,FALSE)

alarm = alarmclock()
timenow = timenow()

thread1 = Thread(target = clockupdate)
thread1.start()

top = Frame(root)
top.pack(side=TOP, fill=X)

clock = StringVar()

timenowlabel = Label(top, textvariable=clock, font=("verdana", 20))
timenowlabel.pack()

body = Frame(root)
body.pack(fill=X)

bottom = Frame(root)
bottom.pack(fill=X, side=BOTTOM)

add = Button(bottom, text="+", width=1, command=alarm.start)
add.pack(side = LEFT)

root.mainloop()
