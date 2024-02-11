import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[ {"role":"user" ,"content":"Mathew perry"} ])
print(completion.choice[0].messages.content)