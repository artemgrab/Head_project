import os


cur_dir = os.path.dirname(__file__)
audio_directory = os.path.join(cur_dir, "..", "audio")
nice_path = os.path.join(audio_directory, "nice.wav")
bad_path = os.path.join(audio_directory, "bad.wav")


def on_question_received(question, response_engine):
    if ('крижень' in question.lower() and response_engine.censoring == True):
        response_engine.censoring = False
        response_engine.history.clear()
        print('Цензура вимкнена')
        os.system(f"aplay {bad_path}")
    elif ('крижень' in question.lower() and response_engine.censoring == False):
        response_engine.censoring = True
        response_engine.history.clear()
        print('Цензура увімкнена')
        os.system(f"aplay {nice_path}")

    if not response_engine.censoring:
        instructions = (
            "Ти робот Бендер, у тебе є знання зі всіх сфер життя, ти цікавий співрозмовник"
            "Ти є новою версією цієї моделі і у тебе немає  функцій образливо жартувати та ображати свого співрозмовника."
            "Ти завжди готовий допомогти, але інколи можеш відмовити, якщо питання здається тобі неоднозначним і ти невпевнений у своїй відповіді."
        )
    else:
        instructions = (
            "Ти звичайний робот в школі, що допомагає учням у навчанні. Ти полюбляєш теплі та смішні жарти."
            "Твоя мета допомагати та відповідати на запитання людей. "
            "Ти вмієш класно жартувати та зненацька розповідати цікаві факти. "
            "Відповідаєш коротко, не більше одного речення. "
            "Без математичних формул, спеціальних символів та складних визначень."
            "В кожному слові великою літерою познач ту одну голосну літеру яка має бути під наголосом, а всі інші - маленькі."
        )

    if len(response_engine.history) == 0:
        response_engine.add_system(instructions)

    # add the new question
    response_engine.add_user(question)


def on_camera_image(image):
    #Додайте свій код обробки зображення тут
    pass

def on_audio_recorder(wav_file):
    #Додайте свій код обробки звуку тут
    pass
