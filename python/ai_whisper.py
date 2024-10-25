import os

import openai
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class Transcription:
    def __init__(self, audiofile):
        self.audiofile = open(audiofile, "rb")

    def write_speech(self):
        result = client.audio.transcriptions.create(model="whisper-1",file=self.audiofile)
        return result

# audio_file = open("../audio/output.wav", "rb")
# transcription = client.audio.transcriptions.create(
#   model="whisper-1",
#   file=audio_file
# )
# print(transcription.text)


