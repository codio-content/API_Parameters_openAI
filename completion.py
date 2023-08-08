import os
import openai
import secret
openai.api_key=secret.api_key

### CODIO SOLUTION BEGIN
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts)

print(response['choices'][0]['text'].strip())
## CODIO SOLUTION END