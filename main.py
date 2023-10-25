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
        # "height": 500,
        "bgcolor": "#2b233c",
        "border_radius": 10,
        "padding": 15,
    }


def prompt_style():
    return {
        # "expand": True,
        "height": 40,
        "width": 420,
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


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"
    # page.bgcolor = "#2c1e4a"

    main = MainContentArea()
    prompt = Prompt(main.chat)

    atomizer_text = Container(
        expand=True,
        content=Text("Atomizer", size=25),
    )
    atomizer_text.padding = padding.only(left=10, right=10)

    page.add(
        Row(
            controls=[
                atomizer_text,
                Container(
                    content=Text("$1,000", size=15, color="#8919db"),
                ),
                Container(
                    alignment=alignment.top_left,
                    content=IconButton(icon=icons.PAYMENT, icon_color="#8919db"),
                ),
            ],
            alignment=MainAxisAlignment.END,
        ),
        main,
        Divider(height=8, color="transparent"),
        prompt,
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
