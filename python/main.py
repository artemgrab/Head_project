from python.audio_recorder import VoiceRecorder
from python.ai_whisper import Transcription
from response import Response
from text_to_speech import AudioResponse
import wave

samples = VoiceRecorder()
samples.record_voice()

transcript = Transcription("../audio/output.wav")
# print(transcript.write_speech())

response = Response(transcript.write_speech())
print(response.get_response())

audio = AudioResponse(response.get_response())
audio.get_audio()


