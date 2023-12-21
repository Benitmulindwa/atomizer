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


# # Example usage
# your_name = "Benit Mulindwa"
# user_question = input("Ask me something: ")
# response = classify_question(user_question)
# print(response)
