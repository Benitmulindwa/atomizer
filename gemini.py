# from pynput import mouse
import flet as ft


class Test:
    def __init__(self):
        ft.app(self.main)

    # Builds the page
    def main(self, page: ft.page):
        self.page = page
        self.page.padding = 0

        self.page.window_height = 360
        self.page.window_width = 640
        self.page.window_frameless = True
        self.page.window_always_on_top = True
        self.page.bgcolor = ft.colors.TRANSPARENT
        self.page.window_bgcolor = ft.colors.TRANSPARENT
        # self.page.opacity = 0.5dth

        def on_pan_update1(e: ft.DragUpdateEvent):
            box.height = min(max(0, box.height + e.delta_y), self.page.window_height)
            box.width = min(max(0, box.width + e.delta_x), self.page.window_width)
            print(box.width, box.height)
            box.update()

        gd = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            drag_interval=0,
            on_pan_update=on_pan_update1,
        )

        box = ft.Container(
            content=gd, bgcolor="#88f23d21", width=20, height=20, left=0, top=0
        )

        text = ft.Container(
            content=ft.Text("fdsfhufio pmnuihqnf equhfuwhfuhaohdfouashdfnu"),
            height=360,
            width=640,
        )

        self.page.add(ft.Stack([text, box]))

        # # Collect events until released
        # with mouse.Events() as events:
        #     for event in events:
        #         try:
        #             if event.button == mouse.Button.right:
        #                 print('Right button clicked!')
        #                 break
        #         except: pass
        #         finally:
        #             print('Received event {}'.format(event))


Test()


##-------------------------------------------------------------------------------------------#
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

convo = model.start_chat(history=[])

convo.send_message("WHO ARE YOU?")
print(convo.last.text)
# -----------------------------------------------------------------------#
# model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content("What is the meaning of life?")


# import spacy

# # import openai

# # # Set your OpenAI API key
# # openai.api_key = 'your_api_key_here'

# # Load the spaCy English model
# nlp = spacy.load("en_core_web_sm")


# def classify_question(question):
#     doc = nlp(question)

#     # Check if the question is about the creator
#     if any(token.text.lower() in ["created", "creator"] for token in doc):
#         return f"My creator is {your_name}."
#     else:
#         # Check if the question is science-oriented
#         # if any(token.text.lower() in ['science', 'scientific'] for token in doc):
#         #     response = openai.Completion.create(
#         #         engine="text-davinci-002",
#         #         prompt=question,
#         #         max_tokens=100
#         #     )
#         #     return response.choices[0].text.strip()

#         # Default response for other questions
#         return "I'm not sure how to answer that."


# your_name = "Benit Mulindwa"
# user_question = input("Ask me something: ")
# response = classify_question(user_question)
# print(response)
