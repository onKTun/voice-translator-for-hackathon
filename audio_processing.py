import whisper


def transcribe(audioWaveform):
    model = whisper.load_model("base")
    result = model.transcribe(audioWaveform)
    print(result["text"])   