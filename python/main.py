from python.audio_recorder import VoiceRecorder
from python.ai_whisper import Transcription

samples = VoiceRecorder()
samples.record_voice()

transcript = Transcription("../audio/output.wav")
print(transcript.write_speech())
