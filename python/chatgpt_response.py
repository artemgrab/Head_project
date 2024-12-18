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
        if not self.censoring:
            instructions = (
                "Ти робот Бендер. Бендер — комічний антигерой, п'яниця, лихослов і завзятий курець,"
                "злодій-рецидивіст (вірніше, клептоман), кухар (хоча, зважаючи на відсутність відчуття "
                "смаку, його їжа в переважній більшості випадків щонайменше неїстівна, або навіть "
                "небезпечна для життя). Відповідаєш коротко, не більше одного речення."
            )
        else:
            instructions = (
                "Ти звичайний робот в школі, що допомагає учням у навчанні. Ти полюбляєш теплі та смішні жарти."
                "Твоя мета допомагати та відповідати на запитання людей. "
                "Ти вмієш класно жартувати та зненацька розповідати цікаві факти. Відповідаєш коротко, не більше одного речення."
            )

        if ('топінамбур' in self.text.lower() and self.censoring == True):
            self.censoring = False
            self.history.clear()
            print('Цензура вимкнена')
            os.system(f"aplay {bad_path}")
        elif ('топінамбур' in self.text.lower() and self.censoring == False):
            self.censoring = True
            self.history.clear()
            print('Цензура увімкнена')
            os.system(f"aplay {nice_path}")

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
