import openai
import flet as ft
from flet import *
import time
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("API_KEY")

openai.api_key = key


def main_style():
    return {
        "expand": True,
        "width": 420,
        "bgcolor": "#2b233c",
        "border_radius": 10,
        "padding": 15,
    }


def prompt_style():
    return {
        "expand": True,
        "height": 40,
        "border_color": "white",
        "content_padding": 10,
        "cursor_color": "white",
    }


class MainContentArea(ft.Container):
    def __init__(self):
        super().__init__(**main_style())
        self.chat = ft.ListView(
            height=200,
            spacing=15,
            auto_scroll=True,
        )
        self.content = self.chat


class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str):
        self.name: str = name
        self.message: str = message
        self.text: str = ft.Text(self.message)
        super().__init__()
        self.controls = [
            ft.Stack(
                [
                    Container(
                        expand=True,
                        bgcolor="red",
                    ),
                    ft.Text(self.name, opacity=0.6, size=20),
                ]
            ),
            self.text,
        ]


class Prompt(ft.TextField):
    def __init__(self, chat: ft.ListView):
        super().__init__(**prompt_style(), on_submit=self.run_prompt)
        self.hint_text = "Ask me anything..."
        self.chat: ListView = chat

    def animate_text(self, name: str, prompt: str):
        word_list: list = []
        msg = CreateMessage(name, "")
        self.chat.controls.append(msg)

        for word in list(prompt):
            word_list.append(word)
            msg.text.value = "".join(word_list)
            self.chat.update()
            time.sleep(0.008)

    def user_output(self, prompt):
        self.animate_text("Me", prompt)

    def gpt_output(self, prompt):
        response: any = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        response: any = response.choices[0].message.content.strip()
        self.animate_text(name="Atomizer", prompt=response)

    def run_prompt(self, event):
        text: any = event.control.value
        self.user_output(prompt=text)
        self.value = ""
        self.update()
        self.gpt_output(prompt=text)
        self.update()


##Style##


def cont_pad(cont: Container, left=10, top=10, right=10, bottom=10):
    cont.padding = padding.only(left, top, right, bottom)
    return cont


def Chat(page):
    main = MainContentArea()
    prompt = Prompt(main.chat)
    atomizer_text = Container(
        expand=True,
        content=Text("Atomizer", size=25),
    )

    def run_prompt(event):
        text: any = prompt.value
        prompt.user_output(prompt=text)
        prompt.value = ""
        prompt.update()
        prompt.gpt_output(prompt=text)
        prompt.update()

    ##Snackbar##

    def snackbar(text):
        page.snack_bar = SnackBar(
            bgcolor="#1d3263",
            open=True,
            duration=1000,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[Text(text, color="white", font_family="lastica")],
            ),
        )
        page.update()

    snackbar("You  have  logged  in  successfully!")
    return Column(
        [
            Row(
                controls=[
                    cont_pad(atomizer_text, top=25),
                    cont_pad(
                        Container(
                            content=Text("$1,000", size=15, color="#8919db"),
                        ),
                        top=25,
                    ),
                    cont_pad(
                        Container(
                            alignment=alignment.top_left,
                            content=IconButton(
                                icon=icons.PAYMENT,
                                icon_color="#8919db",
                            ),
                        ),
                        top=25,
                        right=5,
                    ),
                ],
                alignment=MainAxisAlignment.END,
            ),
            main,
            Divider(height=8, color="transparent"),
            Row(
                controls=[
                    prompt,
                    Container(
                        content=IconButton(
                            icons.ARROW_CIRCLE_UP,
                            icon_size=40,
                            selected_icon_color="#2b233c",
                            on_click=run_prompt,
                        )
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
                spacing=5,
            ),
        ],
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
