import os
import threading
import time
from random import randint, choice

from audio_recorder import VoiceRecorder
from ai_whisper import Transcription
from chatgpt_response import Response
from eyes import BenderEyes
from text_to_speech import AudioResponse

from camera import BenderCamera


POSITION_LEFT = 5
POSITION_MIDDLE = 7.5
POSITION_RIGHT = 10

CURRENT_POSITION = POSITION_MIDDLE

cur_dir = os.path.dirname(__file__)
audio_directory = os.path.join(cur_dir, "..", "audio")


def audio_loop():
    global CURRENT_POSITION
    samples = VoiceRecorder()
    wait_path = os.path.join(audio_directory, "wait.wav")

    history = []
    censoring = False

    while True:
        CURRENT_POSITION = POSITION_MIDDLE
        samples.record_voice()
        # if file doesn't exist, skip
        if os.path.exists("../audio/output.wav"):
            CURRENT_POSITION = POSITION_LEFT
            os.system(f"aplay {wait_path}")
            transcript = Transcription("../audio/output.wav")
            transcribed = transcript.write_speech()
            print(transcribed)

            CURRENT_POSITION = POSITION_RIGHT
            os.system(f"aplay {wait_path}")
            response = Response(transcribed, history, censoring)
            censoring = response.censoring
            r = response.get_response()
            print(r)

            CURRENT_POSITION = POSITION_MIDDLE
            os.system(f"aplay {wait_path}")
            audio = AudioResponse(r)
            audio.get_audio()

            history.append(
                {
                    "role": "user",
                    "content": transcribed
                }
            )
            history.append({
                "role": "assistant",
                "content": r
            })

            if len(history) > 10:
                del history[0]
        else:
            print("No audio input")


def camera_loop():
    camera = BenderCamera()

    while True:
        camera.take_picture()
        time.sleep(5)


def eyes_loop():
    global CURRENT_POSITION
    eyes = BenderEyes()
    #positions = [5, 7.5, 10]
    while True:
        eyes.move(CURRENT_POSITION)
        time.sleep(0.5)
        eyes.move(0)
        time.sleep(1)


def main():
    # new thread for audio loop
    audio_thread = threading.Thread(target=audio_loop)
    audio_thread.start()

    # new thread for camera loop
    camera_thread = threading.Thread(target=camera_loop)
    camera_thread.start()

    # eyes thread
    eyes_thread = threading.Thread(target=eyes_loop)
    eyes_thread.start()

    # wait for both threads to finish
    audio_thread.join()
    camera_thread.join()


if __name__ == "__main__":
    main()
