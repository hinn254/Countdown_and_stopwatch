'''
You can build a desktop application of a countdown timer
 in which the user can set a timer and then when the time is completed, 
 the app will notify the user that the time has ended. 
 It’s a utility app for daily life tasks.
'''

import tkinter

counter = -1
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            # To manage the intial delay
            if counter == -1:
                display = 'Starting...'
            else:
                display = str(counter)

            label.config(text=display) #label['text'] = display 

            # Label.after(arg1, arg2) delays by first argument given in milliseconds
            # and then calls the function given as second argument.Generally like here
            # we need to call the function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000,count)
            counter += 1
    # Triggering the start of the counter
    count()

# start the function of the stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start.config(state='disabled')
    stop.config(state='normal')
    reset.config(state='normal')

#  Stop function of the stopwatch
def Stop():
    global running
    start.config(state='normal')
    stop.config(state='disabled')
    reset.config(state='normal')    
    running = False

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter = -1

    # If reset is pressed after pressing stop
    if running == False:
        reset.config(state='disabled')  # reset['state'] = 'disabled'
        label.config(text='Welcome')    # label['text'] = 'Welcome!'
    # If reset is pressed while the stop watch is running
    else:
        label.config(text='Starting...')# label["text"] = 'Starting...'


root = tkinter.Tk()
root.title('Stopwatch')

# Fixing the window size
root.minsize(width=250,height=70)

label = tkinter.Label(root,text='Welcome',fg='black',font='Verdana 30 bold')
label.pack()

start = tkinter.Button(root, text='Start', width=15, command=lambda:Start(label))
start.pack()

stop = tkinter.Button(root,text='Stop', width=15, state='disabled', command=Stop)
stop.pack()

reset = tkinter.Button(root, text='Reset', width=15, state='disabled',command=lambda:Reset(label))
reset.pack()

root.mainloop()
