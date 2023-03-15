from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def chatgpt_response(prompt):
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     temperature=1,
    #     max_tokens=1000
    # )
    # return response.choices[0].text

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=1000
    )
    if response.choices:
        return response.choices[0].text
    else:
        return "Sorry, I could not generate a response. Please try again with a different prompt."

