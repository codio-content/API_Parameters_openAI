import os
import openai
import secret
openai.api_key=secret.api_key

#CODIO SOLUTION BEGIN
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    top_p=0.8)
for i in (response["choices"]):
  print(i["text"].strip()) 

#CODIO SOLUTION END