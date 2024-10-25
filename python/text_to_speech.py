import os
from dotenv import load_dotenv
from openai import OpenAI
import wave

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class AudioResponse:
    def __init__(self, text):
        self.text = text
        # self.path = path

    def get_audio(self):
        response = client.audio.speech.create(
            model="tts-1",
            voice="echo",
            input=f"{self.text}",
        )
        audio_path = "C:/Users/Artem/OneDrive/Робочий стіл/Head_project/audio/output1.wav"
        response.stream_to_file(audio_path)

        #wave.open(audio_path, "rb")

        # with open("C:/Users/Artem/OneDrive/Робочий стіл/Head_project/audio/output1.wav", "rb") as f:
        #     print(f.read(4))
