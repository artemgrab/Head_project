import os


cur_dir = os.path.dirname(__file__)
audio_directory = os.path.join(cur_dir, "..", "audio")
nice_path = os.path.join(audio_directory, "nice.wav")
bad_path = os.path.join(audio_directory, "bad.wav")


def on_question_received(question, response_engine):
    instructions = ("")

        
    if len(response_engine.history) == 0:
        response_engine.add_system(instructions)

    response_engine.add_user(question)
def on_camera_image(image):
    #Додайте свій код обробки зображення тут
    pass

def on_audio_recorder(wav_file):
    #Додайте свій код обробки звуку тут
    pass
