import whisper
from deep_translator import GoogleTranslator
#import torch
#from TTS.api import TTS
#import numpy as np
from gtts import gTTS
import vlc

def transcribe(audioWaveform):
    model = whisper.load_model("base")
    result = model.transcribe(audioWaveform)
    print(result["text"])
    return result["text"]

def translate(text, language):
    translated = GoogleTranslator(source='auto', target=language).translate(text)  
    print(translated)
    return translated

def speech(input):
    print(input)
    tts = gTTS(input, lang='es')
    tts.save('output.mp3')
    p = vlc.MediaPlayer("output.mp3")
    p.play()

    '''  # Get device
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # List available 🐸TTS models
        #print(TTS().list_models())

        # Init TTS
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

        # Run TTS
        # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
        # Text to speech list of amplitude values as output
        wav = tts.tts(text=input,speaker_wav="/Users/kev/Documents/projects/voice-translator-for-hackathon/record_out.wav", language="en")
        result_list = np.zeros((1, 1))
        for i in range(len(wav)):
            reshaped_array = np.array(wav[i]).reshape(-1, 1)
            result_list = np.r_[result_list, reshaped_array]

        #result = np.concatenate(result_list, axis=0)
        #wav = wav.reshape(-1,1)
        #print(result_list)
        return result_list'''