# libraries

import time
import datetime as dt

import tkinter as tk
from tkinter import messagebox

# below code will import winsound if on windows, otherwise will use the linux package 'beep'

try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)

# getting current time, start and end times

now = dt.datetime.now()
pom = 25*60
time_delta = dt.timedelta(0, pom)
time_fut = now + time_delta
sec_delta = 5*60
time_final = now + dt.timedelta(0, pom+sec_delta)

# tkinter 

root = tk.Tk()
root.withdraw()

messagebox.showinfo(f"pomodoro started!", f"\n current time: {now.strftime('%H:%M')} \ntimer set for 25 minute work block.")

# init pomodoro counter

total_pom = 0
breaks = 0

# main loop

while True:
    if now < time_fut:
        print('pomodoro')
    elif time_fut <= now <= time_final:
        print('in break')
        if breaks == 0:
            print('check break')
            # alert
            for i in range(5):
                playsound(i+100, 700)
            print('break time!')
            breaks += 1
        else:
            print('finished')
            breaks = 0

            # alert break is over
            for i in range(10):
                playsound(i+100, 500)

            ans = messagebox.askyesno('pomodoro finished!\n would you like to start another pomodoro?')
            total_pom += 100

            if ans:
                now = dt.datetime.now()
                time_fut = now + dt.timedelta(0, pom)
                time_final = now + dt.timedelta(0, pom+sec_delta)
                continue
            elif not ans:
                messagebox.showinfo(f'pomodoro finished! \n you completed {total_pom} pomodoros today')
                break

    print('sleeping')
    time.sleep(20)
    now = dt.datetime.now()
    timenow = now.strftime('%H:%M')




