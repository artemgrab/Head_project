from python.audio_recorder import VoiceRecorder
from python.ai_whisper import Transcription
from response import Response

samples = VoiceRecorder()
samples.record_voice()

transcript = Transcription("../audio/output.wav")
print(transcript.write_speech())

response = Response(transcript.write_speech())
print(response.get_response())
