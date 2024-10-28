import os
from dotenv import load_dotenv
from openai import OpenAI
import wave
import sounddevice as sd
import numpy as np

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class AudioResponse:
    def __init__(self, text):
        self.text = text
        # self.path = path

    def get_audio(self):
        # play audio file
        with client.with_streaming_response.audio.speech.create(
                model="tts-1",
                voice="echo",
                input=f"{self.text}",
                response_format="wav"
        ) as response:
            audio_path = "C:/Users/Oleksyi/Desktop/Head_project/audio/output1.wav"
            response.stream_to_file(audio_path)

        # play audio file: read with wave, play with sounddevice

        with wave.open(audio_path, 'rb') as audio_file:
            print("Audio file opened")
            fs = audio_file.getframerate()
            # read all frames
            buffer = audio_file.readframes(-1)
            # convert binary data to integers
            signal = np.frombuffer(buffer, dtype='int16')
            # play audio
            print("Playing audio")
            sd.play(signal, fs)
            # wait until audio is done playing
            sd.wait()
