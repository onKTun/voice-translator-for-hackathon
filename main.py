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
import pyaudio
import sys
import wave
import tkinter


CHUNK = 1024 #how many frames are in one chunk
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5

#creates window for user input
window = tkinter.Tk()
window .title('Vocalation')
button = tkinter.Button(window, text='Push to talk', width=25, command=window.destroy)
button.pack()
window.mainloop()


'''audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)'''




