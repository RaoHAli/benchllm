import openai
openai.api_key ='your-api-key'

import benchllm
from benchllm.input_types import ChatInput


def chat(messages: ChatInput, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response.choices[0].message.content.strip()


@benchllm.test(suite=".")
def gpt_3_5(input: ChatInput):
    return chat(input)
