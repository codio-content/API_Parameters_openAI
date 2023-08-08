import os
import openai
import secret
openai.api_key=secret.api_key

# CODIO SOLUTION BEGIN
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Write a tagline for an ice cream shop",
  temperature=1,
  max_tokens=25,
  best_of=6 )
  
print(response['choices'][0]['text'].strip())
# CODIO SOLUTION END