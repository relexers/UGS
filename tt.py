import time
import winsound
from tkinter import *
from tk import list_screen, loadme

def what_time():
    while True:
        time_list = time.localtime()
        hours = str(time_list[3])
        minut = str(time_list[4])
        secon = str(time_list[5])
        #print (hours + ' часов ' + minut + ' минут ' + secon + ' секунд')
        x = int(hours + minut + secon)
        print (x)
        if x == 75959 or x == 195959:
            winsound.PlaySound('3136.wav', winsound.SND_FILENAME)
            list_screen()
            loadme()
            continue
        elif x == 95959 or x == 215959:
            winsound.PlaySound('3136.wav', winsound.SND_FILENAME)
            list_screen()
            loadme()
            continue
        elif x == 115959 or x == 235959:
            winsound.PlaySound('3136.wav', winsound.SND_FILENAME)
            list_screen()
            loadme()
            continue
        elif x == 135959 or x == 25959:
            winsound.PlaySound('3136.wav', winsound.SND_FILENAME)
            list_screen()
            loadme()
            continue
        elif x == 155959 or x == 35959:
            winsound.PlaySound('3136.wav', winsound.SND_FILENAME)
            list_screen()
            loadme()
            continue
        elif x == 175959 or x == 55959:
            winsound.PlaySound('3136.wav', winsound.SND_FILENAME)
            list_screen()
            loadme()
            continue
        else:
            None	
what_time()
