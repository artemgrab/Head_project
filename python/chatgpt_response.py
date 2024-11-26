import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

history = []

censoring = False

if (censoring==False):
    instructions = "Ти робот Бендер. Бендер — комічний антигерой, п'яниця, лихослов і завзятий курець,"
                            "злодій-рецидивіст (вірніше, клептоман), кухар (хоча, зважаючи на відсутність відчуття "
                            "смаку, його їжа в переважній більшості випадків щонайменше неїстівна, або навіть "
                            "небезпечна для життя)."
elif(censoring==True):
    instructions = "Ти звичайний робот в школі, що допомагає учням у навчанні. Ти полюбляєш теплі та смішні жарти. Твоя мета допомагати та відповідати на запитання людей. Ти вмієш класно жартувати та зненацька розповідати цікаві факти."

class Response:
    def __init__(self, text, history, instructions, censoring):
        self.completion = None
        self.client = client
        self.text = text
        self.history = history
        self.instructions = instructions
        self.censoring = censoring
        
        
        
        
    
    def get_response(self):
            if ('базінга' in self.text.lower() and self.censoring == True):
                self.censoring = False
                print('Цензура вимкнена')
            elif('базінга' in self.text.lower() and self.censoring == False):
                self.censoring = True
                print('Цензура увімкнена')
                
            messages = [
                {"role": "system",
                 "content": f'{self.instructions}'}]
                # ... history
                # {
                #     "role": "user",
                #     "content": f'{self.text}'
                # },]
    
            for question, answer in self.history[-10:]:
                messages.append({ "role": "user", "content": question })
                messages.append({ "role": "assistant", "content": answer }) 
            # add the new question
            messages.append({ "role": "user", "content": self.text })
            self.completion = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
            )
    
            return self.completion.choices[0].message.content


# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()
# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )


# class Response:
#     def __init__(self, text, history):
#         self.completion = None
#         self.client = client
#         self.text = text
#         self.history = history

#     def get_response(self):
#         self.completion = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {"role": "system",
#                  "content": "Ти робот Бендер. Бендер — комічний антигерой, п'яниця, лихослов і завзятий курець,"
#                             "злодій-рецидивіст (вірніше, клептоман), кухар (хоча, зважаючи на відсутність відчуття "
#                             "смаку, його їжа в переважній більшості випадків щонайменше неїстівна, або навіть "
#                             "небезпечна для життя)."},
#                 # ... history
#                 {
#                     "role": "user",
#                     "content": f'{self.text}'
#                 },
#             ]
#         )
        
#         response = self.completion.choices[0].message.content
#         return response
