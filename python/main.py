from audio_recorder import VoiceRecorder
from ai_whisper import Transcription
from chatgpt_response import Response
from text_to_speech import AudioResponse

samples = VoiceRecorder()


while True:
    samples.record_voice()
    transcript = Transcription("../audio/output.wav")
    transcribed = transcript.write_speech()
    print(transcribed)
    response = Response(transcribed)
    r = response.get_response()
    print(r)
    audio = AudioResponse(r)
    audio.get_audio()
