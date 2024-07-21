'''
TODO
get audio input
conditionals for when to transcribe? (above certain threshold?)
direct to transciption
translate the transcription
generate audio out
TTS the translation and direct to audio out
use external software to redirect audio
install ffmopeg

'''
import sounddevice as sd
import sys
import wave
import tkinter
import numpy
from queue import Queue


CHUNK = 1024 #how many frames are in one chunk
#FORMAT = 
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5


translationQueue = Queue(maxsize=5)
audioQueue = Queue()



'''indata: ndarray, outdata: ndarray, frames: int,
         time: CData, status: CallbackFlags'''
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)

    

    audioQueue.put(indata.copy())

def finished_callback():
    print(audioQueue.get())

#audio stream (change to input only)
stream = sd.Stream(callback = callback, finished_callback= finished_callback)




def startRecording(event):
    #add logic to prevent more audio while translation is in progress?
    #or seperate it into a queue?
    if stream.active:
        print("stream is already active")
        return
    
    stream.start()
    print("started audio recording")


    

    

def stopRecording(event):
    if not stream.active:
        print("stream is already inactive")
        return
    
    stream.stop()
    print("recording stopped")

    #method to translate here and output result
    #or maybe just put it in the finished callback? altho might conflict with queue

    


#creates window for user input

window = tkinter.Tk()
window .title('Vocalation')

#change button to call functions on press and release
# https://stackoverflow.com/questions/34522095/gui-button-hold-down-tkinter
button = tkinter.Button(window, text='Push to talk', width=25)
button.pack()
button.bind('<ButtonPress-1>',startRecording)
button.bind('<ButtonRelease-1>',stopRecording)


window.mainloop()









