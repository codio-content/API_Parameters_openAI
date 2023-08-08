import os
import openai
import secret
openai.api_key=secret.api_key

prompts ="Write a tagline for an ice cream shop"

print('Temperature 0.2:')
print('----------------')
for i in range(4):
  response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0.2)

  print(response["choices"][0]["text"].strip())

print('\n\nTemperature 0.8:')
print('----------------')

for i in range(4):
  response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0.8)

  print(response["choices"][0]["text"].strip())