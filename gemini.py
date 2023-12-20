# import pathlib
# import textwrap

# import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown

# from dotenv import load_dotenv

# import os

# load_dotenv()

# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# genai.configure(api_key=GOOGLE_API_KEY)


# def to_markdown(text):
#     text = text.replace("•", "  *")
#     return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


# model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content("What is the meaning of life?")


from flet import *


def main(page: Page):
    def trigger(e):
        e.control.bgcolor = "red" if e.control.bgcolor == "green" else "green"
        e.control.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(
        Container(width=100, height=100, bgcolor="green", on_hover=trigger),
        Container(width=100, height=100, bgcolor="green", on_hover=trigger),
    )
    page.update()


if __name__ == "__main__":
    app(target=main)
