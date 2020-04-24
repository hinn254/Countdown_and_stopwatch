'''
You can build a desktop application of a countdown timer
 in which the user can set a timer and then when the time is completed, 
 the app will notify the user that the time has ended. 
 It’s a utility app for daily life tasks.
'''

import time
import pygame
import notify2

pygame.mixer.init()
pygame.mixer.music.load('alert.wav')

notify2.init('remainder')
n = notify2.Notification('Pythonista',"It's time for a break")
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(11)

print('Please enter time in seconds')
while True:
    try:
        time_to_count = int(input('>>> '))
        while time_to_count >= 0:
            m,s = divmod(time_to_count, 60)
            h,m = divmod(m,60)
            x = str(h).zfill(2) + ':' + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(x,'\r',end='')
            time.sleep(1)
            time_to_count -= 1
            if time_to_count == 0:
                pygame.mixer.music.play()
                n.show()
        print()
    except KeyboardInterrupt:
        print('Program terminated')
        break
    except:
        print("Please enter valid time")