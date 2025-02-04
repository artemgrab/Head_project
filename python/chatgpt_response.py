import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

cur_dir = os.path.dirname(__file__)
audio_directory = os.path.join(cur_dir, "..", "audio")
nice_path = os.path.join(audio_directory, "nice.wav")
bad_path = os.path.join(audio_directory, "bad.wav")


class Response:
    def __init__(self, text, history, censoring):
        self.completion = None
        self.client = client
        self.text = text
        self.history = history
        self.censoring = censoring

    def get_response(self):
        if ('крижень' in self.text.lower() and self.censoring == True):
            self.censoring = False
            self.history.clear()
            print('Цензура вимкнена')
            os.system(f"aplay {bad_path}")
        elif ('крижень' in self.text.lower() and self.censoring == False):
            self.censoring = True
            self.history.clear()
            print('Цензура увімкнена')
            os.system(f"aplay {nice_path}")

        if not self.censoring:
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

        if len(self.history) == 0:
            self.history.append({"role": "system", "content": f'{instructions}'})

        if len(self.history) > 10:
            del self.history[0]

        # add the new question
        self.history.append({ "role": "user", "content": self.text })

        self.completion = client.chat.completions.create(
            model="gpt-4o",
            messages=self.history,
        )
        response = self.completion.choices[0].message.content
        # add the new answer
        self.history.append({ "role": "assistant", "content": response})
        return response
