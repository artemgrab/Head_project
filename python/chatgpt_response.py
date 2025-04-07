import os
from dotenv import load_dotenv
from openai import OpenAI
from integration import on_question_received

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class ResponseEngine:
    def __init__(self, text, history, censoring):
        self.completion = None
        self.client = client
        self.text = text
        self.history = history
        self.censoring = censoring

    def get_response(self):
        on_question_received(self.text, self)

        if len(self.history) > 10:
            del self.history[0]

        self.completion = client.chat.completions.create(
            model="gpt-4o",
            messages=self.history,
        )
        response = self.completion.choices[0].message.content
        # add the new answer
        self.history.append({ "role": "assistant", "content": response})
        return response

    def add_system(self, prompt):
        self.history.append({"role": "system", "content": prompt})

    def add_user(self, prompt):
        self.history.append({"role": "user", "content": prompt})
