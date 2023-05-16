from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_APY_KEY')

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model= "gpt-3.5-turbo",
        prompt=prompt,
        messages= [{"role": "user", "content": "Say this is a test!"}],
        temperature= 0.7,
        max_tokens=100

    )

    response_dict = response.get("chioces")
    if response_dict and len (response_dict) >0:
        prompt_response = response_dict[0]["text"]
    return prompt_response
