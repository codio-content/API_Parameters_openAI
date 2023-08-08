import os
import openai
import secret
openai.api_key=secret.api_key

# Codio solution begins
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    best_of=4)

for i in (response["choices"]):
  print(i["text"].strip()) 


#Codio solution ends