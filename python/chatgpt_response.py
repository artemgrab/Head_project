import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class Response:
    def __init__(self, text):
        self.completion = None
        self.client = client
        self.text = text

    def get_response(self):
        self.completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system",
                 "content": "Ти робот Бендер. Бендер — комічний антигерой, п'яниця, лихослов і завзятий курець,"
                            "злодій-рецидивіст (вірніше, клептоман), кухар (хоча, зважаючи на відсутність відчуття "
                            "смаку, його їжа в переважній більшості випадків щонайменше неїстівна, або навіть "
                            "небезпечна для життя)."},
                {
                    "role": "user",
                    "content": f'{self.text}'
                }
            ]
        )
        
        response = self.completion.choices[0].message.content
        return response
