import os
import openai
openai.api_key = "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"

# customPrompt = input("What do you want to ask the oracle? ")

def run_GPT(gptPrompt):
    response_API = openai.Completion.create(
    model="text-davinci-003",
    prompt=gptPrompt,
    max_tokens=1000,
    temperature=1.1
    )
    return response_API.choices[0].text
