'''
TODO
get audio input
conditionals for when to transcribe? (above certain threshold?)
direct to transciption
translate the transcription
generate audio out
TTS the translation and direct to audio out
use external software to redirect audio


'''
import sounddevice as sd
import sys
import wave
import tkinter
import numpy


CHUNK = 1024 #how many frames are in one chunk
#FORMAT = 
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5

global stream




'''indata: ndarray, outdata: ndarray, frames: int,
         time: CData, status: CallbackFlags'''
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)




def startRecording():
    stream = sd.Stream(callback = callback)
    stream.start()
    if stream.active:
        print("Audio stream is active and recording")
    else:
        print("Start recording called but audio stream is not active")




#creates window for user input
window = tkinter.Tk()
window .title('Vocalation')
#change button to call functions on press and release
# https://stackoverflow.com/questions/34522095/gui-button-hold-down-tkinter
button = tkinter.Button(window, text='Push to talk', width=25, command=startRecording)
button.pack()
window.mainloop()









